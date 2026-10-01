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
        if user_input is None:
            return self.async_show_menu(
                step_id="init",
                menu_options={
                    "settings": "Puzzle settings",
                    "reset_today": "Reset today's puzzle",
                    "reset_all": "Reset all stats",
                },
            )
        return self.async_show_menu(
            step_id="init",
            menu_options={
                "settings": "Puzzle settings",
                "reset_today": "Reset today's puzzle",
                "reset_all": "Reset all stats",
            },
        )

    async def async_step_settings(self, user_input=None):
        if user_input is not None:
            enabled = list(user_input.get(CONF_ENABLED_GAMES) or [])
            if not enabled:
                return self.async_show_form(
                    step_id="settings",
                    data_schema=self._schema(),
                    errors={CONF_ENABLED_GAMES: "at_least_one_game"},
                )
            user_input[CONF_GROUP_MISTAKES] = int(user_input[CONF_GROUP_MISTAKES])
            user_input[CONF_WORD_LENGTH] = int(user_input[CONF_WORD_LENGTH])
            return self.async_create_entry(title="", data=user_input)
        return self.async_show_form(step_id="settings", data_schema=self._schema())

    async def async_step_reset_today(self, user_input=None):
        if user_input is not None:
            if not user_input.get("confirm"):
                return self.async_show_form(
                    step_id="reset_today",
                    data_schema=vol.Schema({vol.Required("confirm", default=False): bool}),
                    errors={"confirm": "confirmation_required"},
                    description_placeholders={"warning": "This clears today's board and reverses today's credited solve, if one was recorded."},
                )
            manager = self.hass.data.get(DOMAIN, {}).get(self.config_entry.entry_id)
            if manager:
                await manager.async_reset_today()
            return self.async_create_entry(title="", data=dict(self.config_entry.options))
        return self.async_show_form(
            step_id="reset_today",
            data_schema=vol.Schema({vol.Required("confirm", default=False): bool}),
            description_placeholders={"warning": "This clears today's board and reverses today's credited solve, if one was recorded."},
        )

    async def async_step_reset_all(self, user_input=None):
        if user_input is not None:
            if not user_input.get("confirm"):
                return self.async_show_form(
                    step_id="reset_all",
                    data_schema=vol.Schema({vol.Required("confirm", default=False): bool}),
                    errors={"confirm": "confirmation_required"},
                    description_placeholders={"warning": "This permanently clears all Daily Puzzle stats and today's board."},
                )
            manager = self.hass.data.get(DOMAIN, {}).get(self.config_entry.entry_id)
            if manager:
                await manager.async_reset_all()
            return self.async_create_entry(title="", data=dict(self.config_entry.options))
        return self.async_show_form(
            step_id="reset_all",
            data_schema=vol.Schema({vol.Required("confirm", default=False): bool}),
            description_placeholders={"warning": "This permanently clears all Daily Puzzle stats and today's board."},
        )

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
