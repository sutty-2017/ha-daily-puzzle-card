from __future__ import annotations

DOMAIN = "daily_puzzle"
NAME = "Daily Puzzle"
PLATFORMS = ["sensor", "binary_sensor"]
STORAGE_VERSION = 1
STORAGE_KEY = "daily_puzzle"

GAME_WORD_GRID = "word_grid"
GAME_FOUR_OF_A_KIND = "four_of_a_kind"
GAME_WORD_WEAVE = "word_weave"
GAME_NAMES = {
    GAME_WORD_GRID: "Word Grid",
    GAME_FOUR_OF_A_KIND: "Four of a Kind",
    GAME_WORD_WEAVE: "Word Weave",
}
DEFAULT_ENABLED_GAMES = list(GAME_NAMES)
CONF_ENABLED_GAMES = "enabled_games"
CONF_ADMIN_MODE = "admin_mode"
CONF_HINTS_ENABLED = "hints_enabled"
CONF_GROUP_MISTAKES = "group_mistakes"
CONF_WORD_LENGTH = "word_length"
DEFAULT_GROUP_MISTAKES = 4
DEFAULT_WORD_LENGTH = 5
