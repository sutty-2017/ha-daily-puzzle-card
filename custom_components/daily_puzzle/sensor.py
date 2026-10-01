from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    manager = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        DailyPuzzleSensor(manager, entry, "status", "Status", "mdi:puzzle"),
        DailyPuzzleSensor(manager, entry, "streak", "Daily streak", "mdi:fire"),
        DailyPuzzleSensor(manager, entry, "best_streak", "Best daily streak", "mdi:trophy"),
        DailyPuzzleSensor(manager, entry, "puzzles_solved", "Puzzles solved", "mdi:check-decagram"),
        DailyPuzzleSensor(manager, entry, "game", "Today's game", "mdi:gamepad-variant"),
    ])


class DailyPuzzleSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, manager, entry, key, name, icon):
        self.manager = manager
        self.key = key
        self._attr_name = name
        self._attr_icon = icon
        self._attr_unique_id = f"{entry.entry_id}_{key}"

    @property
    def native_value(self):
        return self.manager.state.get(self.key)

    @property
    def extra_state_attributes(self):
        if self.key != "status":
            return None
        return {
            "date": self.manager.state.get("date"),
            "game_state": self.manager.state.get("game_state", {}),
            "completed_at": self.manager.state.get("completed_at"),
        }

    async def async_added_to_hass(self):
        self.async_on_remove(self.manager.async_add_listener(self.async_write_ha_state))
