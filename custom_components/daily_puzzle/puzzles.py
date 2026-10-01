from __future__ import annotations

from .const import DEFAULT_ENABLED_GAMES

WORD_PUZZLES = {
    3: ["CAT", "SUN", "MAP", "RED", "BOX", "SKY", "CUP", "FOX", "BEE", "OAK", "SEA", "KEY", "OWL", "PEN", "ICE", "BUS"],
    4: ["FROG", "STAR", "BOOK", "RAIN", "MOON", "TREE", "FISH", "GAME", "BIRD", "WIND", "CAKE", "LAMP", "SNOW", "ROCK", "SHIP", "FIRE"],
    5: ["CRANE", "PLANT", "SHORE", "MUSIC", "LIGHT", "BREAD", "CLOUD", "TRAIN", "HOUSE", "SMILE", "GRAPE", "STONE", "BRICK", "FLAME", "RIVER", "CHAIR", "SWEET", "MOUSE", "BEACH", "DREAM", "CLOCK", "GREEN", "WATER", "SOUND"],
    6: ["PLANET", "GARDEN", "STREAM", "BRIGHT", "POCKET", "WINTER", "FOREST", "CASTLE", "ORANGE", "SILVER", "BRIDGE", "MARKET", "CAMERA", "ISLAND", "BREEZE", "BUTTON"],
    7: ["JOURNEY", "CAPTAIN", "MORNING", "THUNDER", "PICTURE", "RAINBOW", "COUNTRY", "DIAMOND", "KITCHEN", "BALLOON", "LIBRARY", "HARVEST", "COMPASS", "LANTERN", "MYSTERY", "WHISPER"],
}

GROUP_PUZZLES = [
    [
        {"label": "Things that can be sharp", "words": ["KNIFE", "IMAGE", "TURN", "CHEDDAR"]},
        {"label": "Things with keys", "words": ["PIANO", "LOCK", "MAP", "KEYBOARD"]},
        {"label": "___ ball", "words": ["BASE", "CRYSTAL", "CURVE", "DISCO"]},
        {"label": "Kinds of jack", "words": ["BLACK", "UNION", "LUMBER", "MONTEREY"]},
    ],
    [
        {"label": "Can be broken", "words": ["RECORD", "PROMISE", "BONE", "CODE"]},
        {"label": "Found on a desk", "words": ["PEN", "MOUSE", "PAPER", "STAPLER"]},
        {"label": "Types of roll", "words": ["DINNER", "HONOR", "BARREL", "CINNAMON"]},
        {"label": "Go with blue", "words": ["BERRY", "BIRD", "PRINT", "MOON"]},
    ],
    [
        {"label": "Things with a ring", "words": ["PHONE", "BELL", "TREE", "BOXING"]},
        {"label": "Can have a cap", "words": ["BOTTLE", "PEN", "KNEE", "MUSHROOM"]},
        {"label": "Kinds of board", "words": ["DASH", "SURF", "SCORE", "CUTTING"]},
        {"label": "Start with sun", "words": ["FLOWER", "LIGHT", "RISE", "SCREEN"]},
    ],
    [
        {"label": "Things you can pitch", "words": ["TENT", "IDEA", "BALL", "VOICE"]},
        {"label": "Have a shell", "words": ["EGG", "TURTLE", "TACO", "WALNUT"]},
        {"label": "Kinds of table", "words": ["COFFEE", "POOL", "TIMES", "PERIODIC"]},
        {"label": "Can follow fire", "words": ["WORK", "PLACE", "FLY", "WOOD"]},
    ],
]

def game_for_date(day, enabled_games=None):
    games = [game for game in (enabled_games or DEFAULT_ENABLED_GAMES) if game in DEFAULT_ENABLED_GAMES]
    if not games:
        games = list(DEFAULT_ENABLED_GAMES)
    return games[(day.toordinal() * 17 + 7) % len(games)]

def word_for_date(day, length=5):
    words = WORD_PUZZLES.get(int(length), WORD_PUZZLES[5])
    # Give every length its own stable daily answer rather than the same list offset.
    return words[(day.toordinal() * 17 + int(length) * 31) % len(words)]

def word_lengths_for_date(day):
    return {length: word_for_date(day, length) for length in sorted(WORD_PUZZLES)}

def groups_for_date(day):
    return GROUP_PUZZLES[day.toordinal() % len(GROUP_PUZZLES)]
