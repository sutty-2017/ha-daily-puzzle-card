from __future__ import annotations

from datetime import date, timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers.storage import Store
from homeassistant.components.http import StaticPathConfig
from homeassistant.util import dt as dt_util

from .const import DOMAIN, PLATFORMS, STORAGE_KEY, STORAGE_VERSION

DATA_KEY = f"{DOMAIN}_manager"


class DailyPuzzleManager:
    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self.store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
        self.state: dict = {}
        self.listeners = []

    async def async_load(self) -> None:
        self.state = await self.store.async_load() or {
            "date": "",
            "status": "not_started",
            "game": "",
            "game_state": {},
            "streak": 0,
            "best_streak": 0,
            "puzzles_solved": 0,
            "last_solved_date": "",
            "completed_at": None,
        }
        await self.async_rollover()

    async def async_rollover(self) -> None:
        today = dt_util.now().date().isoformat()
        if self.state.get("date") == today:
            return
        self.state.update({
            "date": today,
            "status": "not_started",
            "game": "four_of_a_kind" if dt_util.now().date().toordinal() % 2 else "word_grid",
            "game_state": {},
            "completed_at": None,
        })
        await self.async_save()

    async def async_save(self) -> None:
        await self.store.async_save(self.state)
        for listener in list(self.listeners):
            listener()

    @callback
    def async_add_listener(self, listener):
        self.listeners.append(listener)
        return lambda: self.listeners.remove(listener) if listener in self.listeners else None

    async def async_update_game(self, game: str, game_state: dict, status: str) -> None:
        await self.async_rollover()
        was_solved = self.state.get("status") == "solved"
        self.state["game"] = game
        self.state["game_state"] = game_state
        self.state["status"] = status
        if status == "solved" and not was_solved:
            today = dt_util.now().date()
            last_raw = self.state.get("last_solved_date")
            last = date.fromisoformat(last_raw) if last_raw else None
            self.state["streak"] = self.state.get("streak", 0) + 1 if last == today - timedelta(days=1) else 1
            self.state["best_streak"] = max(self.state.get("best_streak", 0), self.state["streak"])
            self.state["puzzles_solved"] = self.state.get("puzzles_solved", 0) + 1
            self.state["last_solved_date"] = today.isoformat()
            self.state["completed_at"] = dt_util.now().isoformat()
        await self.async_save()


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    manager = DailyPuzzleManager(hass)
    await manager.async_load()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = manager
    hass.data[DATA_KEY] = manager

    await hass.http.async_register_static_paths([
        StaticPathConfig("/daily_puzzle/daily-puzzle-card.js", hass.config.path("custom_components/daily_puzzle/www/daily-puzzle-card.js"), False)
    ])

    async def handle_update(call: ServiceCall) -> None:
        await manager.async_update_game(call.data["game"], call.data.get("game_state", {}), call.data["status"])

    hass.services.async_register(DOMAIN, "update_game", handle_update)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
        hass.data.pop(DATA_KEY, None)
        hass.services.async_remove(DOMAIN, "update_game")
    return unloaded
