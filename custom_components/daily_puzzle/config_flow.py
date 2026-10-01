from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries

from .const import (
    CONF_ADMIN_MODE,
    CONF_ENABLED_GAMES,
    DEFAULT_ENABLED_GAMES,
    DOMAIN,
    GAME_NAMES,
)


class DailyPuzzleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(title="Daily Puzzle", data={})
        return self.async_show_form(step_id="user")

    @staticmethod
    def async_get_options_flow(config_entry):
        return DailyPuzzleOptionsFlow(config_entry)


class DailyPuzzleOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            enabled = list(user_input.get(CONF_ENABLED_GAMES) or [])
            if not enabled:
                return self.async_show_form(
                    step_id="init",
                    data_schema=self._schema(),
                    errors={CONF_ENABLED_GAMES: "at_least_one_game"},
                )
            return self.async_create_entry(title="", data=user_input)
        return self.async_show_form(step_id="init", data_schema=self._schema())

    def _schema(self):
        current = self.config_entry.options
        return vol.Schema({
            vol.Required(
                CONF_ENABLED_GAMES,
                default=current.get(CONF_ENABLED_GAMES, DEFAULT_ENABLED_GAMES),
            ): config_entries.multi_select(GAME_NAMES),
            vol.Required(
                CONF_ADMIN_MODE,
                default=current.get(CONF_ADMIN_MODE, False),
            ): bool,
        })
