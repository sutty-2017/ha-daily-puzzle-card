from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    NumberSelectorMode,
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
)

from .const import (
    CONF_ADMIN_MODE,
    CONF_ENABLED_GAMES,
    CONF_GROUP_MISTAKES,
    CONF_HINTS_ENABLED,
    CONF_WORD_LENGTH,
    DEFAULT_ENABLED_GAMES,
    DEFAULT_GROUP_MISTAKES,
    DEFAULT_WORD_LENGTH,
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
        return DailyPuzzleOptionsFlow()


class DailyPuzzleOptionsFlow(config_entries.OptionsFlowWithReload):
    async def async_step_init(self, user_input=None):
        if user_input is not None:
            enabled = list(user_input.get(CONF_ENABLED_GAMES) or [])
            if not enabled:
                return self.async_show_form(
                    step_id="init",
                    data_schema=self._schema(),
                    errors={CONF_ENABLED_GAMES: "at_least_one_game"},
                )
            user_input[CONF_GROUP_MISTAKES] = int(user_input[CONF_GROUP_MISTAKES])
            user_input[CONF_WORD_LENGTH] = int(user_input[CONF_WORD_LENGTH])
            return self.async_create_entry(title="", data=user_input)
        return self.async_show_form(step_id="init", data_schema=self._schema())

    def _schema(self):
        current = self.config_entry.options
        game_options = [
            SelectOptionDict(value=value, label=label)
            for value, label in GAME_NAMES.items()
        ]
        return vol.Schema({
            vol.Required(
                CONF_ENABLED_GAMES,
                default=current.get(CONF_ENABLED_GAMES, DEFAULT_ENABLED_GAMES),
            ): SelectSelector(
                SelectSelectorConfig(options=game_options, multiple=True)
            ),
            vol.Required(
                CONF_HINTS_ENABLED,
                default=current.get(CONF_HINTS_ENABLED, True),
            ): bool,
            vol.Required(
                CONF_GROUP_MISTAKES,
                default=current.get(CONF_GROUP_MISTAKES, DEFAULT_GROUP_MISTAKES),
            ): NumberSelector(
                NumberSelectorConfig(min=1, max=20, step=1, mode=NumberSelectorMode.BOX)
            ),
            vol.Required(
                CONF_WORD_LENGTH,
                default=current.get(CONF_WORD_LENGTH, DEFAULT_WORD_LENGTH),
            ): NumberSelector(
                NumberSelectorConfig(min=3, max=7, step=1, mode=NumberSelectorMode.BOX)
            ),
            vol.Required(
                CONF_ADMIN_MODE,
                default=current.get(CONF_ADMIN_MODE, False),
            ): bool,
        })
