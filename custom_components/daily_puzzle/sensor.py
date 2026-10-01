from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, NAME

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    manager = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        DailyPuzzleSensor(manager, entry, "status", "Status", "mdi:puzzle"),
        DailyPuzzleSensor(manager, entry, "streak", "Daily streak", "mdi:fire"),
        DailyPuzzleSensor(manager, entry, "best_streak", "Best daily streak", "mdi:trophy"),
        DailyPuzzleSensor(manager, entry, "puzzles_solved", "Puzzles solved", "mdi:check-decagram"),
        DailyPuzzleSensor(manager, entry, "no_hint_solves", "No-hint solves", "mdi:lightbulb-off-outline"),
        DailyPuzzleSensor(manager, entry, "game", "Today's game", "mdi:gamepad-variant"),
        DailyPuzzleSensor(manager, entry, "time_remaining", "Time remaining", "mdi:timer-outline"),
    ])

class DailyPuzzleSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, manager, entry, key, name, icon):
        self.manager = manager
        self.key = key
        self._attr_name = name
        self._attr_icon = icon
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, entry.entry_id)}, name=NAME)

    @property
    def native_value(self):
        if self.key == "time_remaining":
            seconds = self.manager.seconds_remaining()
            hours, rem = divmod(seconds, 3600)
            minutes, secs = divmod(rem, 60)
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        return self.manager.state.get(self.key)

    @property
    def extra_state_attributes(self):
        if self.key == "status":
            return {
                "date": self.manager.state.get("date"),
                "game": self.manager.state.get("game"),
                "game_state": self.manager.public_game_state(),
                "completed": self.manager.state.get("completed", False),
                "completed_at": self.manager.state.get("completed_at"),
                "completed_board": self.manager.state.get("completed_board"),
                "replay_mode": self.manager.state.get("replay_mode", False),
                "test_mode": self.manager.state.get("test_mode", False),
                "admin_mode": self.manager.admin_mode,
                "enabled_games": self.manager.enabled_games,
                "hints_enabled": self.manager.hints_enabled,
                "group_mistakes": self.manager.group_mistakes,
                "credit_lost": self.manager.state.get("credit_lost", False),
            }
        if self.key == "time_remaining":
            return {
                "next_puzzle": self.manager.next_rollover().isoformat(),
                "seconds_remaining": self.manager.seconds_remaining(),
            }
        return None

    async def async_added_to_hass(self):
        self.async_on_remove(self.manager.async_add_listener(self.async_write_ha_state))
