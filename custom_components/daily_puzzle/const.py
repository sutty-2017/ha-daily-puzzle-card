from __future__ import annotations

DOMAIN = "daily_puzzle"
NAME = "Daily Puzzle"
PLATFORMS = ["sensor", "binary_sensor"]
STORAGE_VERSION = 1
STORAGE_KEY = "daily_puzzle"

GAME_WORD_GRID = "word_grid"
GAME_FOUR_OF_A_KIND = "four_of_a_kind"
GAME_NAMES = {
    GAME_WORD_GRID: "Word Grid",
    GAME_FOUR_OF_A_KIND: "Four of a Kind",
}
DEFAULT_ENABLED_GAMES = list(GAME_NAMES)
CONF_ENABLED_GAMES = "enabled_games"
CONF_ADMIN_MODE = "admin_mode"
