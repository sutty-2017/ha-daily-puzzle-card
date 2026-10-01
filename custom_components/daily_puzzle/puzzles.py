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

# Word Weave boards are authored as paths on a 6x6 grid. Every cell belongs
# to exactly one themed answer. The Theme Thread touches opposite grid edges.
WEAVE_PUZZLES = [
    {
        "clue": "A walk in the woods",
        "rows": 6, "cols": 6,
        "words": [
            {"word": "TRAIL", "path": [0, 1, 2, 3, 4]},
            {"word": "MOSS", "path": [5, 11, 10, 9]},
            {"word": "FERN", "path": [8, 7, 6, 12]},
            {"word": "PINE", "path": [13, 14, 15, 16]},
            {"word": "CREEK", "path": [17, 23, 22, 21, 20]},
            {"word": "CANOPY", "path": [19, 18, 24, 25, 26, 27], "thread": True},
            {"word": "ACORN", "path": [28, 29, 35, 34, 33]},
            {"word": "OWL", "path": [32, 31, 30]},
        ],
    },
    {
        "clue": "At the seaside",
        "rows": 6, "cols": 6,
        "words": [
            {"word": "SHELL", "path": [0, 1, 2, 3, 4]},
            {"word": "DUNE", "path": [5, 11, 10, 9]},
            {"word": "TIDE", "path": [8, 7, 6, 12]},
            {"word": "WAVE", "path": [13, 14, 15, 16]},
            {"word": "CORAL", "path": [17, 23, 22, 21, 20]},
            {"word": "COASTS", "path": [19, 18, 24, 25, 26, 27], "thread": True},
            {"word": "SANDY", "path": [28, 29, 35, 34, 33]},
            {"word": "GUL", "path": [32, 31, 30]},
        ],
    },
    {
        "clue": "Cozy kitchen",
        "rows": 6, "cols": 6,
        "words": [
            {"word": "BREAD", "path": [0, 1, 2, 3, 4]},
            {"word": "OVEN", "path": [5, 11, 10, 9]},
            {"word": "SOUP", "path": [8, 7, 6, 12]},
            {"word": "HERB", "path": [13, 14, 15, 16]},
            {"word": "SPICE", "path": [17, 23, 22, 21, 20]},
            {"word": "DINNER", "path": [19, 18, 24, 25, 26, 27], "thread": True},
            {"word": "APPLE", "path": [28, 29, 35, 34, 33]},
            {"word": "TEA", "path": [32, 31, 30]},
        ],
    },
    {
        "clue": "Looking up",
        "rows": 6, "cols": 6,
        "words": [
            {"word": "CLOUD", "path": [0, 1, 2, 3, 4]},
            {"word": "MOON", "path": [5, 11, 10, 9]},
            {"word": "STAR", "path": [8, 7, 6, 12]},
            {"word": "BLUE", "path": [13, 14, 15, 16]},
            {"word": "COMET", "path": [17, 23, 22, 21, 20]},
            {"word": "SKYWAY", "path": [19, 18, 24, 25, 26, 27], "thread": True},
            {"word": "NIGHT", "path": [28, 29, 35, 34, 33]},
            {"word": "SUN", "path": [32, 31, 30]},
        ],
    },
]

def weave_for_date(day):
    puzzle = WEAVE_PUZZLES[day.toordinal() % len(WEAVE_PUZZLES)]
    letters = [""] * (puzzle["rows"] * puzzle["cols"])
    for item in puzzle["words"]:
        for index, char in zip(item["path"], item["word"]):
            letters[index] = char
    return {**puzzle, "letters": letters}

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
