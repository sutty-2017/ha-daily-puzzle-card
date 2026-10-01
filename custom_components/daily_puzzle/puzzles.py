from __future__ import annotations

from itertools import combinations

from .const import DEFAULT_ENABLED_GAMES

WORD_PUZZLES = {
    3: ["CAT","SUN","MAP","RED","BOX","SKY","CUP","FOX","BEE","OAK","SEA","KEY","OWL","PEN","ICE","BUS","ANT","CAR","DOG","EGG","FAN","HAT","JAM","LOG","MUD","NET","PIG","RUN","TOP","VAN","ZIP","AIR","BAT","COW","DAY","EAR","FIG","GEM","HEN","INK","JAR","KID","LID","NUT","PIE","RUG","TOE","WEB","YAK"],
    4: ["FROG","STAR","BOOK","RAIN","MOON","TREE","FISH","GAME","BIRD","WIND","CAKE","LAMP","SNOW","ROCK","SHIP","FIRE","BEAR","BOAT","CAMP","CARD","CLAY","COAT","CROW","DAWN","DEER","DESK","DOOR","DRUM","DUCK","FARM","FLAG","FLOW","GLOW","GOAT","GOLD","GRAY","HILL","HOME","KITE","LAKE","LEAF","LION","MILK","NEST","PARK","PEAR","POND","RING","ROAD","ROPE","ROSE","SALT","SAND","SEAT","SEED","SHOE","SING","SOUP","WAVE","WOLF"],
    5: ["CRANE","PLANT","SHORE","MUSIC","LIGHT","BREAD","CLOUD","TRAIN","HOUSE","SMILE","GRAPE","STONE","BRICK","FLAME","RIVER","CHAIR","SWEET","MOUSE","BEACH","DREAM","CLOCK","GREEN","WATER","SOUND","APPLE","BERRY","BLEND","BLOOM","BRAVE","BRUSH","CANDY","CHARM","CHEST","COAST","CORAL","CREAM","DANCE","EARTH","FIELD","FLOUR","FROST","FRUIT","GLASS","HEART","HONEY","HORSE","JUICE","KNIFE","LEMON","MAPLE","NIGHT","OCEAN","PAINT","PEACH","PIANO","PIZZA","PLANE","RADIO","SHEEP","SHELL","SHINE","SPICE","SPOON","STORM","TABLE","TIGER","TOAST","TRAIL","WHEAT","WORLD"],
    6: ["PLANET","GARDEN","STREAM","BRIGHT","POCKET","WINTER","FOREST","CASTLE","ORANGE","SILVER","BRIDGE","MARKET","CAMERA","ISLAND","BREEZE","BUTTON","ANIMAL","BAKERY","BANANA","BASKET","BOTTLE","BRANCH","CANDLE","CARPET","COFFEE","DINNER","FLOWER","GUITAR","HAMMER","JACKET","KITTEN","MEADOW","MONKEY","NATURE","NEEDLE","PENCIL","PEPPER","PILLOW","RABBIT","ROCKET","SCHOOL","SHADOW","SPRING","SUMMER","SUNSET","TURTLE","VALLEY","WINDOW"],
    7: ["JOURNEY","CAPTAIN","MORNING","THUNDER","PICTURE","RAINBOW","COUNTRY","DIAMOND","KITCHEN","BALLOON","LIBRARY","HARVEST","COMPASS","LANTERN","MYSTERY","WHISPER","AIRPORT","BLANKET","CABINET","CHICKEN","CRYSTAL","DOLPHIN","EVENING","FEATHER","FLOWERS","GIRAFFE","HAMSTER","HOLIDAY","JASMINE","KINGDOM","ORCHARD","PANCAKE","PENGUIN","POPCORN","PUMPKIN","SAILING","SPARROW","SUNRISE","TEACHER","TRACTOR","VILLAGE"],
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
    [
        {"label": "Things with teeth", "words": ["COMB", "SAW", "GEAR", "ZIPPER"]},
        {"label": "Can be cracked", "words": ["EGG", "JOKE", "CODE", "KNUCKLE"]},
        {"label": "Types of wave", "words": ["RADIO", "SOUND", "HEAT", "TIDAL"]},
        {"label": "___ light", "words": ["DAY", "FLASH", "SPOT", "MOON"]},
    ],
    [
        {"label": "Can be folded", "words": ["PAPER", "MAP", "TOWEL", "HANDS"]},
        {"label": "Types of pitch", "words": ["SALES", "PERFECT", "ROOF", "BASEBALL"]},
        {"label": "___ room", "words": ["CLASS", "BED", "MAIL", "COURT"]},
        {"label": "Have strings", "words": ["GUITAR", "PUPPET", "HOODIE", "RACKET"]},
    ],
    [
        {"label": "Found in a wallet", "words": ["CASH", "CARD", "ID", "RECEIPT"]},
        {"label": "Can be streamed", "words": ["MUSIC", "MOVIE", "GAME", "VIDEO"]},
        {"label": "___ case", "words": ["BOOK", "SUIT", "STAIR", "SHOW"]},
        {"label": "Kinds of jam", "words": ["TRAFFIC", "PAPER", "STRAWBERRY", "TOE"]},
    ],
    [
        {"label": "Can be pressed", "words": ["BUTTON", "FLOWER", "SHIRT", "CHARGES"]},
        {"label": "Things with springs", "words": ["MATTRESS", "CLOCK", "TRAMPOLINE", "PEN"]},
        {"label": "___ board", "words": ["KEY", "SURF", "DASH", "SCORE"]},
        {"label": "Kinds of coat", "words": ["RAIN", "LAB", "FUR", "TRENCH"]},
    ],
    [
        {"label": "Can be split", "words": ["BILL", "ATOM", "HAIR", "DECISION"]},
        {"label": "Have a handle", "words": ["DOOR", "MUG", "PAN", "SUITCASE"]},
        {"label": "___ pad", "words": ["NOTE", "MOUSE", "LAUNCH", "KNEE"]},
        {"label": "Can be tied", "words": ["SHOE", "GAME", "SCORE", "APRON"]},
    ],
    [
        {"label": "Can be rolled", "words": ["DICE", "DOUGH", "SLEEVE", "EYES"]},
        {"label": "Have a stem", "words": ["FLOWER", "GLASS", "WATCH", "WORD"]},
        {"label": "___ stone", "words": ["LIME", "SAND", "KEY", "MILE"]},
        {"label": "Kinds of ring", "words": ["WEDDING", "BOXING", "PHONE", "TREE"]},
    ],
    [
        {"label": "Things with roots", "words": ["TREE", "TOOTH", "WORD", "EQUATION"]},
        {"label": "Can be blocked", "words": ["ROAD", "CALL", "SHOT", "DRAIN"]},
        {"label": "___ card", "words": ["POST", "CREDIT", "GIFT", "WILD"]},
        {"label": "Kinds of coat", "words": ["LAB", "RAIN", "FUR", "TRENCH"]},
    ],
    [
        {"label": "Found on a keyboard", "words": ["SPACE", "SHIFT", "ENTER", "TAB"]},
        {"label": "Can have a tail", "words": ["COIN", "COMET", "DOG", "KITE"]},
        {"label": "___ fire", "words": ["CAMP", "WILD", "BON", "CROSS"]},
        {"label": "Kinds of ball", "words": ["BASE", "BASKET", "FOOT", "MEAT"]},
    ],
    [
        {"label": "Can be framed", "words": ["PHOTO", "PERSON", "QUESTION", "HOUSE"]},
        {"label": "Things with a crown", "words": ["KING", "TOOTH", "TREE", "PINEAPPLE"]},
        {"label": "___ break", "words": ["COFFEE", "SPRING", "LUCKY", "JAIL"]},
        {"label": "Kinds of code", "words": ["ZIP", "AREA", "DRESS", "MORSE"]},
    ],
    [
        {"label": "Can be raised", "words": ["HAND", "FLAG", "CHILD", "MONEY"]},
        {"label": "Have a horn", "words": ["CAR", "RHINO", "TRUMPET", "UNICORN"]},
        {"label": "___ cake", "words": ["PAN", "CUP", "CHEESE", "POUND"]},
        {"label": "Kinds of park", "words": ["THEME", "STATE", "WATER", "BALL"]},
    ],
]


# Build a diversified 100-board Four of a Kind rotation from the authored\n# category groups. Index sets are prevalidated to contain 16 unique answers.\n_GROUP_SOURCE = [group for board in GROUP_PUZZLES for group in board]\n_GROUP_BOARD_INDEXES = [[3,6,24,53],[7,10,20,25],[11,22,32,53],[18,25,36,55],[26,28,41,47],[16,35,53,54],[20,25,34,39],[1,2,28,39],[1,4,18,31],[6,29,48,51],[23,36,49,50],[35,40,45,46],[23,34,36,41],[0,43,45,54],[4,15,42,49],[21,22,27,48],[28,33,42,55],[16,19,21,22],[9,18,28,47],[0,14,43,45],[33,42,44,47],[0,3,21,22],[10,36,49,55],[6,13,24,43],[7,25,42,52],[8,21,22,43],[1,4,18,39],[19,21,38,48],[9,10,31,52],[16,21,27,54],[9,28,42,55],[16,21,38,43],[2,7,25,36],[6,21,43,48],[6,13,24,35],[13,19,24,38],[4,18,23,41],[0,5,14,43],[17,42,47,52],[5,6,24,51],[12,15,25,50],[19,21,30,32],[33,44,50,55],[3,14,48,53],[4,15,25,42],[35,40,45,54],[25,47,50,52],[3,24,38,53],[2,23,36,41],[16,27,38,53],[17,26,36,55],[11,14,16,29],[1,10,12,39],[3,40,53,54],[31,33,42,44],[14,32,35,45],[1,10,12,23],[32,35,37,46],[7,20,25,34],[3,5,32,54],[3,14,24,29],[17,34,44,55],[3,21,48,54],[15,17,50,52],[8,19,21,38],[7,12,25,50],[32,38,43,53],[2,12,15,33],[0,35,45,46],[1,18,36,55],[24,27,38,53],[9,15,36,42],[5,38,43,48],[4,25,50,55],[6,27,32,37],[17,23,36,42],[11,24,53,54],[34,36,41,55],[2,4,9,15],[16,29,46,51],[18,20,33,47],[14,21,48,51],[15,26,28,49],[0,37,51,54],[7,17,36,42],[0,29,35,46],[24,35,45,54],[12,17,18,39],[32,38,43,45],[15,41,44,50],[6,19,40,45],[17,34,39,44],[14,24,45,51],[23,28,33,42],[8,11,22,29],[10,41,44,55],[8,14,21,27],[7,18,33,36],[8,11,13,22],[28,33,34,47]]\nGROUP_PUZZLES = [[_GROUP_SOURCE[index] for index in indexes] for indexes in _GROUP_BOARD_INDEXES]\n\n# Word Weave boards use a 6x6 grid. Answers are arranged as adjacent paths;
# every cell belongs to exactly one answer, and the Theme Thread spans top to bottom.
_WEAVE_SETS = [
    ("A walk in the woods", ["TRAIL","MOSS","FERN","PINE","CREEK","CANOPY","ACORN","OWL"], 5),
    ("At the seaside", ["SHELL","DUNE","TIDE","WAVE","CORAL","COASTS","SANDY","SEA"], 5),
    ("Cozy kitchen", ["BREAD","OVEN","SOUP","HERB","SPICE","DINNER","APPLE","TEA"], 5),
    ("Looking up", ["CLOUD","MOON","STAR","BLUE","COMET","HEAVEN","NIGHT","SUN"], 5),
    ("Breakfast table", ["TOAST","EGGS","MILK","OATS","BACON","BRUNCH","HONEY","TEA"], 5),
    ("In the garden", ["TULIP","SOIL","SEED","HOSE","HERBS","GARDEN","BLOOM","BEE"], 5),
    ("Camping trip", ["TENTS","FIRE","HIKE","GEAR","TRAIL","CAMPER","WOODS","MAP"], 5),
    ("Outer space", ["EARTH","MARS","STAR","MOON","COMET","COSMOS","ORBIT","SUN"], 5),
    ("Winter weather", ["FROST","COAT","SNOW","SLED","CHILL","WINTER","GLOVE","ICE"], 5),
    ("Back to school", ["BOOKS","DESK","MATH","BELL","CLASS","SCHOOL","RULER","PEN"], 5),
    ("Road trip", ["MOTEL","ROAD","EXIT","TIRE","MILES","TRAVEL","RADIO","GAS"], 5),
    ("Coffee shop", ["LATTE","BEAN","MUGS","BREW","ROAST","COFFEE","CREAM","CUP"], 5),
    ("Down on the farm", ["HORSE","BARN","CROP","PLOW","WHEAT","FARMER","SHEEP","HEN"], 5),
    ("Pets at home", ["LEASH","BOWL","PAWS","BARK","KITTY","ANIMAL","TREAT","PET"], 5),
    ("At the bakery", ["DONUT","CAKE","ROLL","TART","FLOUR","BAKERY","ICING","PIE"], 5),
    ("Game day", ["FIELD","BALL","TEAM","GOAL","SCORE","SPORTS","COACH","WIN"], 5),
    ("Weather report", ["CLOUD","RAIN","WIND","HAIL","STORM","BREEZE","SUNNY","FOG"], 5),
    ("Under the ocean", ["SHARK","REEF","WAVE","TIDE","WHALE","OCEANS","CORAL","SEA"], 5),
    ("Movie night", ["ACTOR","FILM","ROLE","TAKE","SCENE","CINEMA","DRAMA","CUT"], 5),
    ("Around the house", ["COUCH","DOOR","ROOM","LAMP","TABLE","HOUSES","CHAIR","BED"], 5),
    ("Signs of spring", ["BLOOM","RAIN","BIRD","WARM","GREEN","SPRING","TULIP","BEE"], 5),
]
_WEAVE_PATHS = [
    [1,2,3,4,5],
    [11,10,9,8],
    [7,13,14,15],
    [16,17,23,22],
    [21,20,19,25,26],
    [0,6,12,18,24,30],
    [27,28,29,35,34],
    [33,32,31],
]

def _weave_transform(path, variant):
    def xy(cell):
        return cell % 6, cell // 6
    def cell(x, y):
        return y * 6 + x
    out = []
    for value in path:
        x, y = xy(value)
        if variant == 1:
            x = 5 - x
        elif variant == 2:
            y = 5 - y
        elif variant == 3:
            x, y = 5 - x, 5 - y
        elif variant == 4:
            x, y = y, x
        out.append(cell(x, y))
    return out

def weave_for_date(day):
    # 100 deterministic daily boards: authored themed answer sets are paired
    # with multiple valid grid orientations so the board itself also varies.
    board_index = day.toordinal() % 100
    clue, words, thread_index = _WEAVE_SETS[board_index % len(_WEAVE_SETS)]
    variant = (board_index // len(_WEAVE_SETS)) % 5
    paths = [_weave_transform(path, variant) for path in _WEAVE_PATHS]
    letters = [""] * 36
    answers = []
    for index, (word, path) in enumerate(zip(words, paths)):
        for cell_index, char in zip(path, word):
            letters[cell_index] = char
        answers.append({"word": word, "path": path, "thread": index == thread_index})
    return {"clue": clue, "rows": 6, "cols": 6, "letters": letters, "words": answers}

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
