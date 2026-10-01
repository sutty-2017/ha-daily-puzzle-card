from __future__ import annotations

import asyncio
import json
import logging
from datetime import date, timedelta
from pathlib import Path

import voluptuous as vol
from homeassistant.components.http import StaticPathConfig
from homeassistant.components.lovelace.const import LOVELACE_DATA
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.event import async_track_time_interval, async_track_utc_time_change
from homeassistant.helpers.storage import Store
from homeassistant.util import dt as dt_util

from .const import (CONF_ADMIN_MODE, CONF_ENABLED_GAMES, CONF_GROUP_MISTAKES, CONF_HINTS_ENABLED, DEFAULT_ENABLED_GAMES, DEFAULT_GROUP_MISTAKES, DOMAIN, GAME_NAMES, PLATFORMS, STORAGE_KEY, STORAGE_VERSION)
from .puzzles import game_for_date, groups_for_date, word_for_date

_LOGGER = logging.getLogger(__name__)
DATA_KEY = f"{DOMAIN}_manager"
_CARD_FILENAME = "daily-puzzle-card.js"
_CARD_PATH = Path(__file__).parent / "www" / _CARD_FILENAME
_MANIFEST_PATH = Path(__file__).parent / "manifest.json"
_CARD_VERSION = json.loads(_MANIFEST_PATH.read_text(encoding="utf-8"))["version"]
_CARD_STATIC_URL = f"/daily_puzzle/{_CARD_FILENAME}"
_CARD_URL = f"{_CARD_STATIC_URL}?v={_CARD_VERSION}"

def _word_score(answer: str, guess: str) -> list[str]:
    result = ["absent"] * len(answer)
    counts: dict[str, int] = {}
    for i, char in enumerate(guess):
        if char == answer[i]:
            result[i] = "correct"
        else:
            counts[answer[i]] = counts.get(answer[i], 0) + 1
    for i, char in enumerate(guess):
        if result[i] == "correct":
            continue
        if counts.get(char, 0):
            result[i] = "present"
            counts[char] -= 1
    return result

class DailyPuzzleManager:
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.entry = entry
        self.store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
        self.state: dict = {}
        self.listeners = []
        self.unsubs = []

    async def async_load(self) -> None:
        self.state = await self.store.async_load() or {
            "date": "", "status": "not_started", "game": "", "game_state": {},
            "streak": 0, "best_streak": 0, "puzzles_solved": 0, "no_hint_solves": 0,
            "last_solved_date": "", "completed": False, "completed_at": None,
            "completed_board": None, "replay_mode": False, "test_mode": False,
        }
        self.state.setdefault("completed", self.state.get("status") == "solved")
        self.state.setdefault("completed_board", None)
        self.state.setdefault("replay_mode", False)
        self.state.setdefault("test_mode", False)
        self.state.setdefault("daily_snapshot", None)
        self.state.setdefault("credit_lost", False)
        self.state.setdefault("no_hint_solves", 0)
        # v0.2.1 Word Grid boards were always five letters. Preserve an underway
        # or completed board instead of forcing a new length choice on upgrade.
        if self.state.get("game") == "word_grid":
            game_state = dict(self.state.get("game_state") or {})
            if not game_state.get("word_length") and (
                game_state.get("guesses") or self.state.get("status") in ("in_progress", "solved", "failed")
            ):
                game_state["word_length"] = 5
                self.state["game_state"] = game_state
            completed_board = self.state.get("completed_board")
            if isinstance(completed_board, dict) and completed_board.get("guesses") and not completed_board.get("word_length"):
                completed_board = dict(completed_board)
                completed_board["word_length"] = 5
                self.state["completed_board"] = completed_board
        if self.state.get("test_mode") and not self.admin_mode and self.state.get("daily_snapshot"):
            self.state.update(self.state["daily_snapshot"])
            self.state["test_mode"] = False
            self.state["daily_snapshot"] = None
        await self.async_rollover()

    def start_timers(self) -> None:
        @callback
        def _minute(_now):
            self.hass.async_create_task(self.async_rollover())
            self.async_notify()

        @callback
        def _midnight(_now):
            self.hass.async_create_task(self.async_rollover())

        self.unsubs.append(async_track_time_interval(self.hass, _minute, timedelta(minutes=1)))
        self.unsubs.append(async_track_utc_time_change(self.hass, _midnight, minute=0, second=0))

    def stop_timers(self) -> None:
        for unsub in self.unsubs:
            unsub()
        self.unsubs.clear()

    @property
    def enabled_games(self) -> list[str]:
        games = list(self.entry.options.get(CONF_ENABLED_GAMES, DEFAULT_ENABLED_GAMES))
        return [game for game in games if game in GAME_NAMES] or list(DEFAULT_ENABLED_GAMES)

    @property
    def admin_mode(self) -> bool:
        return bool(self.entry.options.get(CONF_ADMIN_MODE, False))

    @property
    def hints_enabled(self) -> bool:
        return bool(self.entry.options.get(CONF_HINTS_ENABLED, True))

    @property
    def group_mistakes(self) -> int:
        return max(1, int(self.entry.options.get(CONF_GROUP_MISTAKES, DEFAULT_GROUP_MISTAKES)))

    def _new_game_state(self, game: str, day: date) -> dict:
        return {"mistake_limit": self.group_mistakes} if game == "four_of_a_kind" else {}

    async def async_rollover(self) -> None:
        today_date = dt_util.now().date()
        today = today_date.isoformat()
        if self.state.get("date") == today:
            return
        last_raw = self.state.get("last_solved_date")
        if last_raw and date.fromisoformat(last_raw) < today_date - timedelta(days=1):
            self.state["streak"] = 0
        self.state.update({
            "date": today, "status": "not_started", "game": game_for_date(today_date, self.enabled_games),
            "game_state": self._new_game_state(game_for_date(today_date, self.enabled_games), today_date), "completed": False, "completed_at": None,
            "completed_board": None, "replay_mode": False, "test_mode": False, "daily_snapshot": None, "credit_lost": False,
        })
        await self.async_save()

    def next_rollover(self):
        now = dt_util.now()
        return now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

    def seconds_remaining(self) -> int:
        return max(0, int((self.next_rollover() - dt_util.now()).total_seconds()))

    def public_game_state(self) -> dict:
        day = date.fromisoformat(self.state["date"])
        data = dict(self.state.get("game_state") or {})
        if self.state["game"] == "four_of_a_kind":
            groups = groups_for_date(day)
            data["words"] = [word for group in groups for word in group["words"]]
            solved_words = {word for group in data.get("solved_groups", []) for word in group["words"]}
            used_groups = set(data.get("hint_group_indexes") or [])
            data["hint_available"] = len(data.get("hint_pairs") or []) < 2 and any(
                index not in used_groups and len([word for word in group["words"] if word not in solved_words]) >= 2
                for index, group in enumerate(groups)
            )
        elif self.state["game"] == "word_grid":
            length = int(data.get("word_length") or 0)
            data["word_lengths"] = [3, 4, 5, 6, 7]
            if length:
                answer = word_for_date(day, length)
                found = {char for guess in data.get("guesses", []) for char, score in zip(guess["word"], guess["score"]) if score in ("present", "correct")}
                found.update(data.get("hint_letters") or [])
                used = set(data.get("hint_types") or [])
                vowels = set("AEIOU")
                data["hint_available_types"] = [
                    kind for kind, letters in (
                        ("consonant", [c for c in answer if c not in vowels and c not in found]),
                        ("vowel", [c for c in answer if c in vowels and c not in found]),
                    ) if kind not in used and letters
                ]
            else:
                data["hint_available_types"] = []
        return data

    async def async_submit_word(self, guess: str) -> None:
        await self.async_rollover()
        if self.state["game"] != "word_grid":
            return
        guess = guess.strip().upper()
        game_state = dict(self.state.get("game_state") or {})
        length = int(game_state.get("word_length") or 0)
        if length not in (3, 4, 5, 6, 7) or len(guess) != length or not guess.isalpha() or self.state["status"] == "solved":
            return
        day = date.fromisoformat(self.state["date"])
        answer = word_for_date(day, length)
        guesses = list(game_state.get("guesses") or [])
        if len(guesses) >= 6:
            return
        guesses.append({"word": guess, "score": _word_score(answer, guess)})
        game_state["guesses"] = guesses
        self.state["game_state"] = game_state
        if guess == answer:
            self.state["status"] = "solved"
            await self._async_complete()
        elif len(guesses) >= 6:
            self.state["status"] = "failed"
            self._mark_failed_attempt()
        else:
            self.state["status"] = "in_progress"
        await self.async_save()

    async def async_select_word_length(self, length: int) -> None:
        await self.async_rollover()
        if self.state["game"] != "word_grid" or self.state["status"] != "not_started":
            return
        length = int(length)
        if length not in (3, 4, 5, 6, 7):
            return
        game_state = dict(self.state.get("game_state") or {})
        game_state["word_length"] = length
        game_state.setdefault("guesses", [])
        self.state["game_state"] = game_state
        await self.async_save()

    async def async_submit_group(self, words: list[str]) -> None:
        await self.async_rollover()
        if self.state["game"] != "four_of_a_kind" or self.state["status"] in ("solved", "failed"):
            return
        selected = {str(word).strip().upper() for word in words}
        if len(selected) != 4:
            return
        day = date.fromisoformat(self.state["date"])
        groups = groups_for_date(day)
        game_state = dict(self.state.get("game_state") or {})
        solved = list(game_state.get("solved_groups") or [])
        solved_words = {word for group in solved for word in group["words"]}
        match = next((g for g in groups if set(g["words"]) == selected and not selected <= solved_words), None)
        if not match:
            mistakes = int(game_state.get("mistakes", 0)) + 1
            game_state["mistakes"] = mistakes
            game_state["last_result"] = "incorrect"
            self.state["game_state"] = game_state
            if mistakes >= int(game_state.get("mistake_limit", self.group_mistakes)):
                self.state["status"] = "failed"
                self._mark_failed_attempt()
            else:
                self.state["status"] = "in_progress"
            await self.async_save()
            return
        solved.append({"label": match["label"], "words": list(match["words"])})
        game_state["solved_groups"] = solved
        game_state["last_result"] = "correct"
        self.state["game_state"] = game_state
        self.state["status"] = "solved" if len(solved) == 4 else "in_progress"
        if len(solved) == 4:
            await self._async_complete()
        await self.async_save()

    def _mark_failed_attempt(self) -> None:
        if self.state.get("test_mode") or self.state.get("replay_mode") or self.state.get("completed"):
            return
        self.state["credit_lost"] = True
        self.state["streak"] = 0

    async def _async_complete(self) -> None:
        if self.state.get("test_mode") or self.state.get("completed"):
            return
        self.state["completed"] = True
        self.state["completed_at"] = dt_util.now().isoformat()
        self.state["completed_board"] = json.loads(json.dumps(self.state.get("game_state") or {}))
        if self.state.get("credit_lost") or self.state.get("replay_mode"):
            return
        today = dt_util.now().date()
        last_raw = self.state.get("last_solved_date")
        last = date.fromisoformat(last_raw) if last_raw else None
        self.state["streak"] = self.state.get("streak", 0) + 1 if last == today - timedelta(days=1) else 1
        self.state["best_streak"] = max(self.state.get("best_streak", 0), self.state["streak"])
        self.state["puzzles_solved"] = self.state.get("puzzles_solved", 0) + 1
        if int((self.state.get("game_state") or {}).get("hints_used", 0)) == 0:
            self.state["no_hint_solves"] = self.state.get("no_hint_solves", 0) + 1
        self.state["last_solved_date"] = today.isoformat()

    def _capture_daily_snapshot(self) -> None:
        if self.state.get("test_mode") or self.state.get("daily_snapshot"):
            return
        keys = ("game", "game_state", "status", "completed", "completed_at", "completed_board", "replay_mode", "credit_lost")
        self.state["daily_snapshot"] = {key: json.loads(json.dumps(self.state.get(key))) for key in keys}

    async def async_admin_reset(self) -> None:
        await self.async_rollover()
        if not self.admin_mode:
            return
        self._capture_daily_snapshot()
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["test_mode"] = True
        await self.async_save()

    async def async_admin_switch_game(self, game: str) -> None:
        await self.async_rollover()
        if not self.admin_mode or game not in GAME_NAMES:
            return
        self._capture_daily_snapshot()
        self.state["game"] = game
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["test_mode"] = True
        await self.async_save()

    async def async_return_to_daily(self) -> None:
        await self.async_rollover()
        if not self.admin_mode:
            return
        snapshot = self.state.get("daily_snapshot")
        if snapshot:
            self.state.update(snapshot)
        else:
            today = dt_util.now().date()
            game = game_for_date(today, self.enabled_games)
            self.state["game"] = game
            self.state["game_state"] = {}
            self.state["status"] = "not_started"
            self.state["replay_mode"] = False
        self.state["test_mode"] = False
        self.state["daily_snapshot"] = None
        await self.async_save()

    async def async_replay(self) -> None:
        await self.async_rollover()
        if self.state.get("test_mode"):
            old_state = dict(self.state.get("game_state") or {})
            self.state["game_state"] = self._new_game_state(self.state["game"], date.fromisoformat(self.state["date"]))
            if self.state["game"] == "word_grid" and old_state.get("word_length"):
                self.state["game_state"]["word_length"] = old_state["word_length"]
            self.state["status"] = "not_started"
            await self.async_save()
            return
        if self.state.get("status") not in ("solved", "failed") and not self.state.get("completed"):
            return
        old_state = dict(self.state.get("game_state") or {})
        self.state["game_state"] = self._new_game_state(self.state["game"], date.fromisoformat(self.state["date"]))
        if self.state["game"] == "word_grid":
            length = old_state.get("word_length")
            if not length and isinstance(self.state.get("completed_board"), dict):
                length = self.state["completed_board"].get("word_length")
            if length:
                self.state["game_state"]["word_length"] = length
        self.state["status"] = "not_started"
        self.state["replay_mode"] = True
        await self.async_save()


    async def async_use_hint(self) -> None:
        await self.async_rollover()
        if not self.hints_enabled or self.state.get("status") in ("solved", "failed"):
            return
        day = date.fromisoformat(self.state["date"])
        game_state = dict(self.state.get("game_state") or {})
        if self.state["game"] == "word_grid":
            length = int(game_state.get("word_length") or 0)
            if length not in (3, 4, 5, 6, 7):
                return
            answer = word_for_date(day, length)
            guesses = list(game_state.get("guesses") or [])
            found = {
                char
                for guess in guesses
                for char, score in zip(guess["word"], guess["score"])
                if score in ("present", "correct")
            }
            hinted = list(game_state.get("hint_letters") or [])
            found.update(hinted)
            vowels = set("AEIOU")
            consonants = [c for c in answer if c not in vowels and c not in found]
            vowel_letters = [c for c in answer if c in vowels and c not in found]
            used_types = list(game_state.get("hint_types") or [])
            if "consonant" not in used_types and consonants:
                hinted.append(consonants[0])
                used_types.append("consonant")
            elif "vowel" not in used_types and vowel_letters:
                hinted.append(vowel_letters[0])
                used_types.append("vowel")
            else:
                return
            game_state["hint_letters"] = hinted
            game_state["hint_types"] = used_types
        elif self.state["game"] == "four_of_a_kind":
            groups = groups_for_date(day)
            solved_words = {word for group in game_state.get("solved_groups", []) for word in group["words"]}
            pairs = list(game_state.get("hint_pairs") or [])
            hinted_group_indexes = list(game_state.get("hint_group_indexes") or [])
            candidate = None
            candidate_index = None
            for index, group in enumerate(groups):
                available = [word for word in group["words"] if word not in solved_words]
                if index not in hinted_group_indexes and len(available) >= 2:
                    candidate = available[:2]
                    candidate_index = index
                    break
            if not candidate or len(pairs) >= 2:
                return
            pairs.append(candidate)
            hinted_group_indexes.append(candidate_index)
            game_state["hint_pairs"] = pairs
            game_state["hint_group_indexes"] = hinted_group_indexes
        else:
            return
        game_state["hints_used"] = int(game_state.get("hints_used", 0)) + 1
        self.state["game_state"] = game_state
        if self.state["status"] == "not_started":
            self.state["status"] = "in_progress"
        await self.async_save()

    async def async_save(self) -> None:
        await self.store.async_save(self.state)
        self.async_notify()

    @callback
    def async_notify(self) -> None:
        for listener in list(self.listeners):
            listener()

    @callback
    def async_add_listener(self, listener):
        self.listeners.append(listener)
        return lambda: self.listeners.remove(listener) if listener in self.listeners else None

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    manager = DailyPuzzleManager(hass, entry)
    await manager.async_load()
    manager.start_timers()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = manager
    hass.data[DATA_KEY] = manager

    async def submit_word(call: ServiceCall) -> None:
        await manager.async_submit_word(call.data["guess"])

    async def select_word_length(call: ServiceCall) -> None:
        await manager.async_select_word_length(call.data["length"])

    async def submit_group(call: ServiceCall) -> None:
        await manager.async_submit_group(call.data["words"])

    async def replay(call: ServiceCall) -> None:
        await manager.async_replay()

    async def admin_reset(call: ServiceCall) -> None:
        await manager.async_admin_reset()

    async def admin_switch_game(call: ServiceCall) -> None:
        await manager.async_admin_switch_game(call.data["game"])

    async def return_to_daily(call: ServiceCall) -> None:
        await manager.async_return_to_daily()

    async def use_hint(call: ServiceCall) -> None:
        await manager.async_use_hint()

    hass.services.async_register(DOMAIN, "submit_word", submit_word, schema=vol.Schema({vol.Required("guess"): cv.string}))
    hass.services.async_register(DOMAIN, "select_word_length", select_word_length, schema=vol.Schema({vol.Required("length"): vol.All(vol.Coerce(int), vol.In([3, 4, 5, 6, 7]))}))
    hass.services.async_register(DOMAIN, "submit_group", submit_group, schema=vol.Schema({vol.Required("words"): vol.All(cv.ensure_list, [cv.string])}))
    hass.services.async_register(DOMAIN, "replay", replay)
    hass.services.async_register(DOMAIN, "admin_reset", admin_reset)
    hass.services.async_register(DOMAIN, "admin_switch_game", admin_switch_game, schema=vol.Schema({vol.Required("game"): vol.In(GAME_NAMES)}))
    hass.services.async_register(DOMAIN, "return_to_daily", return_to_daily)
    hass.services.async_register(DOMAIN, "use_hint", use_hint)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    hass.async_create_task(_async_register_frontend(hass))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        manager = hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
        if manager:
            manager.stop_timers()
        hass.data.pop(DATA_KEY, None)
        for service in ("submit_word", "select_word_length", "submit_group", "replay", "admin_reset", "admin_switch_game", "return_to_daily", "use_hint"):
            hass.services.async_remove(DOMAIN, service)
    return unloaded

async def _async_register_frontend(hass: HomeAssistant) -> None:
    done_key = f"{DOMAIN}_frontend_registered"
    task_key = f"{DOMAIN}_frontend_task"
    if hass.data.get(done_key):
        return
    existing_task = hass.data.get(task_key)
    if existing_task and not existing_task.done():
        return

    async def _register_with_retries() -> None:
        for _ in range(60):
            try:
                if not _CARD_PATH.exists():
                    _LOGGER.warning("Daily Puzzle card file not found: %s", _CARD_PATH)
                    return
                static_key = f"{DOMAIN}_static_registered"
                if not hass.data.get(static_key):
                    await hass.http.async_register_static_paths([
                        StaticPathConfig(_CARD_STATIC_URL, str(_CARD_PATH), cache_headers=True)
                    ])
                    hass.data[static_key] = True
                lovelace_data = hass.data.get(LOVELACE_DATA)
                if lovelace_data is None:
                    await asyncio.sleep(2)
                    continue
                resources = getattr(lovelace_data, "resources", None)
                if resources is None:
                    await asyncio.sleep(2)
                    continue
                if hasattr(resources, "loaded") and not resources.loaded:
                    await resources.async_load()
                items = list(resources.async_items())
                matches = [item for item in items if str(item.get("url", "")).startswith(_CARD_STATIC_URL)]
                if hasattr(resources, "async_update_item"):
                    if matches:
                        primary = matches[0]
                        if primary.get("url") != _CARD_URL:
                            await resources.async_update_item(primary["id"], {"res_type": "module", "url": _CARD_URL})
                        for duplicate in matches[1:]:
                            await resources.async_delete_item(duplicate["id"])
                    else:
                        await resources.async_create_item({"res_type": "module", "url": _CARD_URL})
                elif not any(item.get("url") == _CARD_URL for item in items):
                    _LOGGER.warning("Daily Puzzle cannot update Lovelace resources in YAML mode. Add %s as a module resource.", _CARD_URL)
                hass.data[done_key] = True
                return
            except Exception as err:  # noqa: BLE001
                _LOGGER.debug("Waiting to register Daily Puzzle card: %s", err)
                await asyncio.sleep(2)
        _LOGGER.warning("Could not automatically register Daily Puzzle card. Add %s as a module resource if needed.", _CARD_URL)

    task = hass.async_create_task(_register_with_retries())
    hass.data[task_key] = task
    task.add_done_callback(lambda _future: hass.data.pop(task_key, None))
    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, lambda _event: hass.async_create_task(_register_with_retries()))
