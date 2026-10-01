from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, NAME

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    async_add_entities([DailyPuzzleCompleted(hass.data[DOMAIN][entry.entry_id], entry)])

class DailyPuzzleCompleted(BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_name = "Completed"
    _attr_icon = "mdi:check-circle"

    def __init__(self, manager, entry):
        self.manager = manager
        self._attr_unique_id = f"{entry.entry_id}_completed"
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, entry.entry_id)}, name=NAME)

    @property
    def is_on(self):
        return bool(self.manager.state.get("completed"))

    @property
    def extra_state_attributes(self):
        return {
            "date": self.manager.state.get("date"),
            "completed_at": self.manager.state.get("completed_at"),
            "replay_mode": self.manager.state.get("replay_mode", False),
        }

    async def async_added_to_hass(self):
        self.async_on_remove(self.manager.async_add_listener(self.async_write_ha_state))
