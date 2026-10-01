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

from .const import (CONF_ADMIN_MODE, CONF_ENABLED_GAMES, DEFAULT_ENABLED_GAMES, DOMAIN, GAME_NAMES, PLATFORMS, STORAGE_KEY, STORAGE_VERSION)
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
    result = ["absent"] * 5
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
            "streak": 0, "best_streak": 0, "puzzles_solved": 0,
            "last_solved_date": "", "completed": False, "completed_at": None,
            "completed_board": None, "replay_mode": False, "test_mode": False,
        }
        self.state.setdefault("completed", self.state.get("status") == "solved")
        self.state.setdefault("completed_board", None)
        self.state.setdefault("replay_mode", False)
        self.state.setdefault("test_mode", False)
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

    def _new_game_state(self, game: str, day: date) -> dict:
        return {}

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
            "completed_board": None, "replay_mode": False, "test_mode": False,
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
            data["words"] = [word for group in groups_for_date(day) for word in group["words"]]
        return data

    async def async_submit_word(self, guess: str) -> None:
        await self.async_rollover()
        if self.state["game"] != "word_grid":
            return
        guess = guess.strip().upper()
        if len(guess) != 5 or not guess.isalpha() or self.state["status"] == "solved":
            return
        day = date.fromisoformat(self.state["date"])
        answer = word_for_date(day)
        game_state = dict(self.state.get("game_state") or {})
        guesses = list(game_state.get("guesses") or [])
        if len(guesses) >= 6:
            return
        guesses.append({"word": guess, "score": _word_score(answer, guess)})
        game_state["guesses"] = guesses
        self.state["game_state"] = game_state
        self.state["status"] = "solved" if guess == answer else "in_progress"
        if guess == answer:
            await self._async_complete()
        await self.async_save()

    async def async_submit_group(self, words: list[str]) -> None:
        await self.async_rollover()
        if self.state["game"] != "four_of_a_kind" or self.state["status"] == "solved":
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
            game_state["last_result"] = "incorrect"
            self.state["game_state"] = game_state
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

    async def _async_complete(self) -> None:
        if self.state.get("test_mode") or self.state.get("completed"):
            return
        today = dt_util.now().date()
        last_raw = self.state.get("last_solved_date")
        last = date.fromisoformat(last_raw) if last_raw else None
        self.state["completed"] = True
        self.state["completed_at"] = dt_util.now().isoformat()
        self.state["completed_board"] = json.loads(json.dumps(self.state.get("game_state") or {}))
        self.state["streak"] = self.state.get("streak", 0) + 1 if last == today - timedelta(days=1) else 1
        self.state["best_streak"] = max(self.state.get("best_streak", 0), self.state["streak"])
        self.state["puzzles_solved"] = self.state.get("puzzles_solved", 0) + 1
        self.state["last_solved_date"] = today.isoformat()

    async def async_admin_reset(self) -> None:
        await self.async_rollover()
        if not self.admin_mode:
            return
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["test_mode"] = True
        await self.async_save()

    async def async_admin_switch_game(self, game: str) -> None:
        await self.async_rollover()
        if not self.admin_mode or game not in GAME_NAMES:
            return
        self.state["game"] = game
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["test_mode"] = True
        await self.async_save()

    async def async_return_to_daily(self) -> None:
        await self.async_rollover()
        if not self.admin_mode:
            return
        today = dt_util.now().date()
        game = game_for_date(today, self.enabled_games)
        self.state["game"] = game
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["test_mode"] = False
        self.state["replay_mode"] = False
        await self.async_save()

    async def async_replay(self) -> None:
        await self.async_rollover()
        if not self.state.get("completed"):
            return
        self.state["game_state"] = {}
        self.state["status"] = "not_started"
        self.state["replay_mode"] = True
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

    hass.services.async_register(DOMAIN, "submit_word", submit_word, schema=vol.Schema({vol.Required("guess"): cv.string}))
    hass.services.async_register(DOMAIN, "submit_group", submit_group, schema=vol.Schema({vol.Required("words"): vol.All(cv.ensure_list, [cv.string])}))
    hass.services.async_register(DOMAIN, "replay", replay)
    hass.services.async_register(DOMAIN, "admin_reset", admin_reset)
    hass.services.async_register(DOMAIN, "admin_switch_game", admin_switch_game, schema=vol.Schema({vol.Required("game"): vol.In(GAME_NAMES)}))
    hass.services.async_register(DOMAIN, "return_to_daily", return_to_daily)

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
        for service in ("submit_word", "submit_group", "replay", "admin_reset", "admin_switch_game", "return_to_daily"):
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
