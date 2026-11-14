"""Content and manager regression tests, without requiring an HA installation.

The real manager class is compiled with small storage/clock boundary doubles.
HA integration loading itself remains a release-stage check.
"""
import ast
import asyncio
from collections import Counter
from datetime import date, datetime, timedelta
import importlib
import json
from pathlib import Path
import sys
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'custom_components/daily_puzzle'
pkg = types.ModuleType('daily_puzzle')
pkg.__path__ = [str(PACKAGE)]
sys.modules['daily_puzzle'] = pkg
const = importlib.import_module('daily_puzzle.const')
puzzles = importlib.import_module('daily_puzzle.puzzles')
links = importlib.import_module('daily_puzzle.links')

class Store:
    def __init__(self, *args): self.saved = None
    async def async_save(self, state): self.saved = json.loads(json.dumps(state))
    async def async_load(self): return self.saved

clock = types.SimpleNamespace(now=lambda: datetime(2026, 11, 13, 12))
namespace = dict(vars(const), date=date, timedelta=timedelta, json=json, Store=Store,
                 dt_util=clock, callback=lambda fn: fn, HomeAssistant=object,
                 ConfigEntry=object, links_for_date=links.links_for_date,
                 **{name: getattr(puzzles, name) for name in ('game_for_date', 'groups_for_date', 'weave_for_date', 'word_for_date')})
source = ast.parse((PACKAGE / '__init__.py').read_text())
selected = [node for node in source.body if getattr(node, 'name', None) in ('DailyPuzzleManager', '_word_score', 'async_migrate_entry')]
exec(compile(ast.Module(body=selected, type_ignores=[]), str(PACKAGE / '__init__.py'), 'exec'), namespace)
Manager = namespace['DailyPuzzleManager']

class ContentTests(unittest.TestCase):
    def test_frozen_library(self):
        content = json.loads((PACKAGE/'word_links.json').read_text())
        boards = content['boards']
        edges = set(map(tuple, content['approved_links']))
        self.assertEqual(len(boards), 220)
        self.assertEqual(len(set(map(tuple, boards))), 220)
        self.assertEqual(len(set(board[0] for board in boards)), 220)
        for board in boards + [item['words'] for item in content['holidays'].values()]:
            self.assertEqual(len(board), 7)
            self.assertEqual(len(set(board)), 7)
            self.assertTrue(all(word.isascii() and word.isalpha() and word.isupper() for word in board))
            self.assertTrue(all(pair in edges for pair in zip(board, board[1:])), board)
        self.assertEqual(set(content['holidays']), set(puzzles._HOLIDAY_WORDS))

    def test_random_choice(self):
        start = date(2026, 11, 14)
        days = [start + timedelta(days=i) for i in range(2000)]
        games = [puzzles.game_for_date(day) for day in days]
        self.assertEqual(games, [puzzles.game_for_date(day) for day in days])
        self.assertEqual(set(games), set(const.DEFAULT_ENABLED_GAMES))
        self.assertTrue(all(350 < count < 650 for count in Counter(games).values()))
        self.assertTrue(any(a == b for a, b in zip(games, games[1:])))
        self.assertEqual(puzzles.game_for_date(start, ['word_links']), 'word_links')
        self.assertNotIn('word_links', [puzzles.game_for_date(day, ['word_grid', 'word_weave']) for day in days])

    def test_holiday_calendar_and_cycle(self):
        seen = set()
        for i in range(366):
            day = date(2028, 1, 1) + timedelta(days=i)
            holiday = puzzles.holiday_for_date(day)
            board = links.links_for_date(day)
            if holiday:
                seen.add(holiday)
                self.assertEqual(board['words'], links.HOLIDAY_LINKS[holiday]['words'])
                self.assertTrue(board['theme'])
            self.assertEqual(board, links.links_for_date(day))
        self.assertEqual(seen, set(links.HOLIDAY_LINKS))
        # Normal-day selection visits the full 220 calendar slots; holiday slots
        # intentionally take precedence and may postpone a normal board.
        found = {links.links_for_date(date(2026, 1, 1)+timedelta(days=i))['id'] for i in range(1500)}
        self.assertTrue(all(f'links-{i:03}' in found for i in range(1, 221)))

class ManagerTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        clock.now = lambda: datetime(2026, 11, 13, 12)
        self.entry = types.SimpleNamespace(options={'admin_mode': True, 'enabled_games': ['word_links']})
        self.m = Manager(types.SimpleNamespace(), self.entry)
        await self.m.async_load()
        self.words = links.links_for_date(date(2026, 11, 13))['words']

    async def guess(self, word, **overrides):
        public = self.m.public_game_state()
        args = {'guess': word, 'puzzle_date': self.m.state['date'], 'index': public['active_index'], 'revision': public['revision']}
        args.update(overrides)
        await self.m.async_submit_link(**args)

    async def solve(self):
        for word in self.words[len(self.m.state['game_state']['solved_words'])+1:]:
            await self.guess(word)

    async def test_public_clues_no_answers(self):
        state = self.m.public_game_state()
        self.assertEqual(state['rows'][0], self.words[0])
        for clue, word in zip(state['rows'][1:], self.words[1:]):
            self.assertEqual(clue, word[0] + '_' * (len(word)-1))
        self.assertNotIn('words', state)
        self.assertFalse(self.m.state['completed'])

    async def test_complete_replay_and_reset_credit(self):
        await self.solve()
        original = json.loads(json.dumps(self.m.state['completed_board']))
        self.assertEqual(self.m.state['puzzles_solved'], 1)
        self.assertEqual(self.m.state['no_hint_solves'], 1)
        await self.m.async_replay()
        self.assertTrue(self.m.state['completed'])
        self.assertEqual(self.m.state['completed_board'], original)
        await self.solve()
        self.assertEqual(self.m.state['puzzles_solved'], 1)
        self.assertEqual(self.m.state['completed_board'], original)
        await self.m.async_reset_today()
        self.assertEqual(self.m.state['puzzles_solved'], 0)
        self.assertFalse(self.m.state['completed'])

    async def test_hint_limits_and_no_hint_stats(self):
        await self.m.async_use_hint()
        self.assertEqual(self.m.public_game_state()['rows'][1][:2], self.words[1][:2])
        await self.guess(self.words[1])
        await self.m.async_use_hint()
        await self.m.async_use_hint()
        self.assertEqual(self.m.state['game_state']['hints_used'], 2)
        self.assertFalse(self.m.public_game_state()['hint_available'])
        await self.solve()
        self.assertEqual(self.m.state['puzzles_solved'], 1)
        self.assertEqual(self.m.state['no_hint_solves'], 0)

    async def test_hint_disabled(self):
        self.entry.options['hints_enabled'] = False
        await self.m.async_use_hint()
        self.assertEqual(self.m.state['game_state']['hints_used'], 0)

    async def test_fail_reveal_retry(self):
        wrong = 'Z' * len(self.words[1])
        for _ in range(6): await self.guess(wrong)
        self.assertEqual(self.m.state['status'], 'failed')
        await self.m.async_use_hint()
        await self.guess(self.words[1])
        self.assertEqual(self.m.state['status'], 'failed')
        await self.m.async_reveal_answer()
        self.assertEqual(self.m.public_game_state()['rows'], self.words)
        self.assertFalse(self.m.state['completed'])
        self.assertEqual(self.m.state['puzzles_solved'], 0)
        await self.m.async_replay()
        await self.solve()
        self.assertTrue(self.m.state['completed'])
        self.assertEqual(self.m.state['puzzles_solved'], 0)

    async def test_duplicate_stale_invalid_requests(self):
        await self.guess('!')
        await self.guess(self.words[1], puzzle_date='2026-11-12')
        await self.guess(self.words[1], index=2)
        self.assertEqual(self.m.state['status'], 'not_started')
        await asyncio.gather(self.guess(self.words[1], index=1, revision=0), self.guess(self.words[1], index=1, revision=0))
        self.assertEqual(self.m.state['game_state']['solved_words'], [self.words[1]])
        wrong = 'Z' * len(self.words[2])
        await asyncio.gather(self.guess(wrong, index=2, revision=1), self.guess(wrong, index=2, revision=1))
        self.assertEqual(self.m.state['game_state']['mistakes'], 1)

    async def test_test_mode_and_return(self):
        await self.guess(self.words[1])
        original = json.loads(json.dumps(self.m.state))
        await self.m.async_admin_switch_game('word_links')
        await self.solve()
        self.assertEqual(self.m.state['puzzles_solved'], 0)
        await self.m.async_return_to_daily()
        self.assertEqual(self.m.state['game_state'], original['game_state'])
        self.assertEqual(self.m.state['status'], original['status'])

    async def test_reload_and_rollover(self):
        await self.guess(self.words[1])
        await self.m.async_load()
        self.assertEqual(self.m.state['game_state']['solved_words'], [self.words[1]])
        clock.now = lambda: datetime(2026, 11, 14, 0, 1)
        await self.m.async_rollover()
        self.assertEqual(self.m.state['date'], '2026-11-14')
        self.assertEqual(self.m.state['game_state']['solved_words'], [])
        await self.guess(self.words[1], puzzle_date='2026-11-13')
        self.assertEqual(self.m.state['status'], 'not_started')

    async def test_upgrade_keeps_existing_board_and_restrictive_options(self):
        changes=[]
        hass=types.SimpleNamespace(config_entries=types.SimpleNamespace(async_update_entry=lambda entry, **kw: changes.append(kw)))
        for enabled, expected in [(['word_grid','four_of_a_kind','word_weave'], const.DEFAULT_ENABLED_GAMES), (['word_grid'], ['word_grid'])]:
            entry=types.SimpleNamespace(options={'enabled_games': enabled}, version=1, minor_version=1)
            self.assertTrue(await namespace['async_migrate_entry'](hass, entry))
            self.assertEqual(changes[-1]['options']['enabled_games'], expected)
        self.m.state['game']='word_grid'
        self.m.state['game_state']={'word_length': 5, 'guesses': []}
        await self.m.async_save()
        await self.m.async_load()
        self.assertEqual(self.m.state['game'], 'word_grid')
        self.assertEqual(self.m.state['game_state'], {'word_length': 5, 'guesses': []})

    async def test_existing_games_still_solve(self):
        day=date(2026,11,13)
        for game in ['word_grid', 'four_of_a_kind', 'word_weave']:
            await self.m.async_admin_switch_game(game)
            if game=='word_grid': await self.m.async_submit_word(puzzles.word_for_date(day, self.m.word_length))
            elif game=='four_of_a_kind':
                for group in puzzles.groups_for_date(day): await self.m.async_submit_group(group['words'])
            else:
                for word in puzzles.weave_for_date(day)['words']: await self.m.async_submit_weave(word['path'])
            self.assertEqual(self.m.state['status'], 'solved', game)
            self.assertEqual(self.m.state['puzzles_solved'], 0)

if __name__ == '__main__': unittest.main()
