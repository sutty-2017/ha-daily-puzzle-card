from __future__ import annotations

from .const import DEFAULT_ENABLED_GAMES
from .four_content import EXPANDED_GROUP_BOARDS

WORD_PUZZLES = {
    3: ["CAT","SUN","MAP","RED","BOX","SKY","CUP","FOX","BEE","OAK","SEA","KEY","OWL","PEN","ICE","BUS","ANT","CAR","DOG","EGG","FAN","HAT","JAM","LOG","MUD","NET","PIG","RUN","TOP","VAN","ZIP","AIR","BAT","COW","DAY","EAR","FIG","GEM","HEN","INK","JAR","KID","LID","NUT","PIE","RUG","TOE","WEB","YAK"],
    4: ["FROG","STAR","BOOK","RAIN","MOON","TREE","FISH","GAME","BIRD","WIND","CAKE","LAMP","SNOW","ROCK","SHIP","FIRE","BEAR","BOAT","CAMP","CARD","CLAY","COAT","CROW","DAWN","DEER","DESK","DOOR","DRUM","DUCK","FARM","FLAG","FLOW","GLOW","GOAT","GOLD","GRAY","HILL","HOME","KITE","LAKE","LEAF","LION","MILK","NEST","PARK","PEAR","POND","RING","ROAD","ROPE","ROSE","SALT","SAND","SEAT","SEED","SHOE","SING","SOUP","WAVE","WOLF"],
    5: ["CRANE","PLANT","SHORE","MUSIC","LIGHT","BREAD","CLOUD","TRAIN","HOUSE","SMILE","GRAPE","STONE","BRICK","FLAME","RIVER","CHAIR","SWEET","MOUSE","BEACH","DREAM","CLOCK","GREEN","WATER","SOUND","APPLE","BERRY","BLEND","BLOOM","BRAVE","BRUSH","CANDY","CHARM","CHEST","COAST","CORAL","CREAM","DANCE","EARTH","FIELD","FLOUR","FROST","FRUIT","GLASS","HEART","HONEY","HORSE","JUICE","KNIFE","LEMON","MAPLE","NIGHT","OCEAN","PAINT","PEACH","PIANO","PIZZA","PLANE","RADIO","SHEEP","SHELL","SHINE","SPICE","SPOON","STORM","TABLE","TIGER","TOAST","TRAIL","WHEAT","WORLD","ABOUT","ABOVE","ABUSE","ACTOR","ACUTE","ADMIT","ADOPT","ADULT","AFTER","AGAIN","AGENT","AGREE","AHEAD","ALARM","ALBUM","ALERT","ALIKE","ALIVE","ALLOW","ALONE","ALONG","ALTER","AMONG","ANGER","ANGLE","ANGRY","APART","APPLY","ARGUE","ARISE","ARRAY","ASIDE","ASSET","AUDIO","AUDIT","AVOID","AWARD","AWARE","BADLY","BAKER","BASES","BASIC","BASIN","BASIS","BATCH","BATHE","BEGAN","BEGIN","BEGUN","BEING","BELOW","BENCH","BIRTH","BLACK","BLAME","BLANK","BLAST","BLIND","BLOCK","BLOOD","BOARD","BOOST","BOOTH","BOUND","BRAIN","BRAND","BREAK","BREED","BRIEF","BRING","BROAD","BROKE","BROWN","BUILD","BUILT","BUYER","CABLE","CARRY","CATCH","CAUSE","CHAIN","CHART","CHASE","CHEAP","CHECK","CHEEK","CHILD","CHINA","CHOSE","CIVIL","CLAIM","CLASS","CLEAN","CLEAR","CLIMB","CLOSE","COACH","COLOR","COULD","COUNT","COURT","COVER","CRAFT","CRASH","CROSS","CROWD","CROWN","CURVE","CYCLE","DAILY","DEALT","DEATH","DELAY","DEPTH","DOING","DOUBT","DOZEN","DRAFT","DRAMA","DRAWN","DRESS","DRINK","DRIVE","DROVE","DYING","EAGER","EARLY","EIGHT","ELBOW","ELDER","ELECT","EMPTY","ENEMY","ENJOY","ENTER","ENTRY","EQUAL","ERROR","EVENT","EVERY","EXACT","EXIST","EXTRA","FAITH","FALSE","FAULT","FAVOR","FIBER","FIFTH","FIFTY","FIGHT","FINAL","FIRST","FIXED","FLASH","FLEET","FLOOR","FOCUS","FORCE","FORTH","FORTY","FORUM","FOUND","FRAME","FRESH","FRONT","FULLY","FUNNY","GIANT","GIVEN","GLOBE","GOING","GRACE","GRADE","GRAND","GRANT","GRASS","GREAT","GROUP","GROWN","GUARD","GUESS","GUEST","GUIDE","HAPPY","HEAVY","HENCE","IDEAL","IMAGE","INDEX","INNER","INPUT","ISSUE","JOINT","JUDGE","KNOWN","LABEL","LARGE","LASER","LATER","LAUGH","LAYER","LEARN","LEAST","LEAVE","LEGAL","LEVEL","LOCAL","LOGIC","LOOSE","LOWER","LUCKY","LUNCH","MAJOR","MAKER","MARCH","MATCH","MAYBE","MAYOR","METAL","MIGHT","MINOR","MODEL","MONEY","MONTH","MOTOR","MOUNT","MOVIE","NEEDS","NEVER","NEWLY","NORTH","NOVEL","NURSE","OCCUR","OFFER","OFTEN","ORDER","OTHER","OUGHT","OWNER","PANEL","PAPER","PARTY","PEACE","PHASE","PHONE","PHOTO","PIECE","PILOT","PITCH","PLACE","PLAIN","POINT","POUND","POWER","PRESS","PRICE","PRIDE","PRIME","PRINT","PRIOR","PRIZE","PROOF","PROUD","QUEEN","QUICK","QUIET","QUITE","RAISE","RANGE","RAPID","REACH","READY","RIGHT","ROUND","ROUTE","ROYAL","RURAL","SCALE","SCENE","SCOPE","SCORE","SENSE","SERVE","SEVEN","SHALL","SHAPE","SHARE","SHARP","SHEET","SHELF","SHIFT","SHIRT","SHOCK","SHOOT","SHORT","SHOWN","SIGHT","SINCE"],
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


# v0.3.3 used 56 authored groups. Keep that exact bank for historical dates.
_LEGACY_GROUP_SOURCE = [group for board in GROUP_PUZZLES for group in board]
_LEGACY_GROUP_BOARD_INDEXES = [[3,6,24,53],[7,10,20,25],[11,22,32,53],[18,25,36,55],[26,28,41,47],[16,35,53,54],[20,25,34,39],[1,2,28,39],[1,4,18,31],[6,29,48,51],[23,36,49,50],[35,40,45,46],[23,34,36,41],[0,43,45,54],[4,15,42,49],[21,22,27,48],[28,33,42,55],[16,19,21,22],[9,18,28,47],[0,14,43,45],[33,42,44,47],[0,3,21,22],[10,36,49,55],[6,13,24,43],[7,25,42,52],[8,21,22,43],[1,4,18,39],[19,21,38,48],[9,10,31,52],[16,21,27,54],[9,28,42,55],[16,21,38,43],[2,7,25,36],[6,21,43,48],[6,13,24,35],[13,19,24,38],[4,18,23,41],[0,5,14,43],[17,42,47,52],[5,6,24,51],[12,15,25,50],[19,21,30,32],[33,44,50,55],[3,14,48,53],[4,15,25,42],[35,40,45,54],[25,47,50,52],[3,24,38,53],[2,23,36,41],[16,27,38,53],[17,26,36,55],[11,14,16,29],[1,10,12,39],[3,40,53,54],[31,33,42,44],[14,32,35,45],[1,10,12,23],[32,35,37,46],[7,20,25,34],[3,5,32,54],[3,14,24,29],[17,34,44,55],[3,21,48,54],[15,17,50,52],[8,19,21,38],[7,12,25,50],[32,38,43,53],[2,12,15,33],[0,35,45,46],[1,18,36,55],[24,27,38,53],[9,15,36,42],[5,38,43,48],[4,25,50,55],[6,27,32,37],[17,23,36,42],[11,24,53,54],[34,36,41,55],[2,4,9,15],[16,29,46,51],[18,20,33,47],[14,21,48,51],[15,26,28,49],[0,37,51,54],[7,17,36,42],[0,29,35,46],[24,35,45,54],[12,17,18,39],[32,38,43,45],[15,41,44,50],[6,19,40,45],[17,34,39,44],[14,24,45,51],[23,28,33,42],[8,11,22,29],[10,41,44,55],[8,14,21,27],[7,18,33,36],[8,11,13,22],[28,33,34,47]]
_LEGACY_GROUP_PUZZLES = [[_LEGACY_GROUP_SOURCE[index] for index in indexes] for indexes in _LEGACY_GROUP_BOARD_INDEXES]

# v0.4.0 expands the authored bank to 300 category groups. Build 300
# deterministic boards while rejecting any board with a repeated answer.
_GROUP_SOURCE = _LEGACY_GROUP_SOURCE + [group for board in EXPANDED_GROUP_BOARDS for group in board]

def _build_group_puzzles():
    boards = []
    signatures = set()
    cursor = 0
    count = len(_GROUP_SOURCE)
    while len(boards) < 300 and cursor < 100000:
        value = cursor + 1
        chosen = set()
        while len(chosen) < 4:
            value = (1664525 * value + 1013904223) & 0xFFFFFFFF
            chosen.add(value % count)
        indexes = tuple(sorted(chosen))
        cursor += 1
        if indexes in signatures:
            continue
        groups = [_GROUP_SOURCE[index] for index in indexes]
        words = [word for group in groups for word in group["words"]]
        if len(set(words)) != 16:
            continue
        signatures.add(indexes)
        boards.append(groups)
    if len(boards) != 300:
        raise RuntimeError("Unable to build 300 unique Four of a Kind boards")
    return boards

GROUP_PUZZLES = _build_group_puzzles()

# Special-date puzzle overrides. These use the actual calendar holiday date,
# not an alternate federal employee "in lieu of" workday.
def _nth_weekday(year, month, weekday, n):
    from datetime import date, timedelta
    first = date(year, month, 1)
    return first + timedelta(days=(weekday - first.weekday()) % 7 + 7 * (n - 1))

def _last_weekday(year, month, weekday):
    from datetime import date, timedelta
    next_month = date(year + (month == 12), 1 if month == 12 else month + 1, 1)
    last = next_month - timedelta(days=1)
    return last - timedelta(days=(last.weekday() - weekday) % 7)

def holiday_for_date(day):
    fixed = {(1,1):"new_year",(2,14):"valentines",(3,17):"st_patricks",(6,19):"juneteenth",(7,4):"independence",(10,31):"halloween",(11,11):"veterans",(12,25):"christmas"}
    hit = fixed.get((day.month, day.day))
    if hit:
        return hit
    moving = {
        _nth_weekday(day.year,1,0,3):"mlk",
        _nth_weekday(day.year,2,0,3):"presidents",
        _last_weekday(day.year,5,0):"memorial",
        _nth_weekday(day.year,9,0,1):"labor",
        _nth_weekday(day.year,10,0,2):"columbus",
        _nth_weekday(day.year,11,3,4):"thanksgiving",
    }
    return moving.get(day)

_HOLIDAY_WORDS = {
"new_year":"CLOCK","mlk":"DREAM","presidents":"CIVIC","memorial":"HONOR",
"juneteenth":"UNITY","independence":"STARS","labor":"CRAFT","columbus":"OCEAN",
"veterans":"HONOR","thanksgiving":"FEAST","christmas":"HOLLY",
"valentines":"HEART","st_patricks":"GREEN","halloween":"GHOST",
}
_HOLIDAY_WEAVES = {
"new_year":("New Year's Eve",["CLOCK","YEAR","HOPE","BELL","PARTY","CHEERS","TOAST","NEW"],5),
"mlk":("Dr. Martin Luther King Jr. Day",["DREAM","HOPE","VOTE","LEAD","PEACE","RIGHTS","UNITY","ACT"],5),
"presidents":("Presidents Day",["WHITE","OVAL","VOTE","FLAG","CIVIC","LEADER","UNION","USA"],5),
"memorial":("Memorial Day",["HONOR","FLAG","TAPS","NAME","BRAVE","SALUTE","STONE","USA"],5),
"juneteenth":("Juneteenth",["UNITY","FREE","HOPE","SONG","DANCE","RIGHTS","BLACK","JOY"],5),
"independence":("Independence Day",["STARS","FLAG","BOOM","JULY","SPARK","PARADE","EAGLE","USA"],5),
"labor":("Labor Day",["CRAFT","WORK","TOOL","TEAM","SHIFT","WORKER","UNION","JOB"],5),
"columbus":("Exploration Day",["OCEAN","SHIP","SAIL","MAPS","NORTH","VOYAGE","CHART","SEA"],5),
"veterans":("Veterans Day",["HONOR","DUTY","FLAG","ARMY","BRAVE","SALUTE","MEDAL","USA"],5),
"thanksgiving":("Thanksgiving",["FEAST","YAMS","CORN","TART","GRAVY","TURKEY","THANK","PIE"],5),
"christmas":("Christmas",["HOLLY","GIFT","STAR","BELL","ANGEL","WREATH","SANTA","JOY"],5),
"valentines":("Valentine's Day",["HEART","LOVE","ROSE","DATE","CANDY","KISSES","CUPID","HUG"],5),
"st_patricks":("St. Patrick's Day",["GREEN","LUCK","HARP","EIRE","CHARM","CLOVER","LEAFY","JIG"],5),
"halloween":("Halloween",["GHOST","MASK","DARK","CAPE","WITCH","CANDLE","TREAT","BOO"],5),
}

_HOLIDAY_GROUPS = {
"new_year":[("At midnight",["CLOCK","COUNTDOWN","KISS","CHEERS"]),("Fresh starts",["GOAL","PLAN","RESOLVE","BEGIN"]),("Party supplies",["HAT","HORN","CONFETTI","BALLOON"]),("Calendar words",["YEAR","MONTH","WEEK","DATE"])],
"mlk":[("Community action",["SERVE","MARCH","VOTE","LEAD"]),("Values",["JUSTICE","PEACE","EQUALITY","UNITY"]),("Public speaking",["SPEECH","PODIUM","CROWD","MIC"]),("Ways to help",["GIVE","TEACH","LISTEN","BUILD"])],
"presidents":[("White House",["OVAL","DESK","CABINET","EAST"]),("Election words",["VOTE","BALLOT","POLL","TICKET"]),("U.S. government",["SENATE","HOUSE","COURT","CONGRESS"]),("National symbols",["FLAG","EAGLE","SEAL","STARS"])],
"memorial":[("Remembrance",["HONOR","MEMORY","TRIBUTE","WREATH"]),("Ceremony",["FLAG","SALUTE","SILENCE","BUGLE"]),("Military branches",["ARMY","NAVY","MARINES","AIRFORCE"]),("At a memorial",["STONE","NAME","FLOWERS","VISITOR"])],
"juneteenth":[("Celebration",["MUSIC","PARADE","PICNIC","FESTIVAL"]),("Freedom",["LIBERTY","RIGHTS","CHOICE","VOICE"]),("Community",["FAMILY","FRIENDS","NEIGHBOR","UNITY"]),("Summer gathering",["PARK","FOOD","GAMES","DANCE"])],
"independence":[("Fourth of July",["FIREWORKS","PARADE","PICNIC","FLAG"]),("Patriotic symbols",["EAGLE","STARS","STRIPES","LIBERTY"]),("Cookout",["GRILL","BURGER","CORN","MELON"]),("Night sky",["SPARK","BURST","GLOW","BOOM"])],
"labor":[("On the job",["SHIFT","CLOCK","BREAK","PAY"]),("Tools",["HAMMER","DRILL","WRENCH","LEVEL"]),("Workplaces",["OFFICE","SHOP","SITE","PLANT"]),("Teamwork",["CREW","GROUP","PARTNER","LEADER"])],
"columbus":[("Navigation",["MAP","COMPASS","CHART","BEARING"]),("At sea",["SHIP","SAIL","DECK","MAST"]),("Ocean travel",["VOYAGE","PORT","WAVE","HORIZON"]),("Explorer gear",["ROPE","CHEST","CLOAK","BOOTS"])],
"veterans":[("Service",["DUTY","HONOR","COURAGE","SACRIFICE"]),("Military branches",["ARMY","NAVY","MARINES","AIRFORCE"]),("Ceremony",["FLAG","SALUTE","PARADE","SPEECH"]),("Uniform items",["BOOT","CAP","BADGE","MEDAL"])],
"thanksgiving":[("On the table",["TURKEY","GRAVY","STUFFING","CRANBERRY"]),("Desserts",["PIE","CAKE","TART","COOKIE"]),("Harvest",["CORN","GOURD","APPLE","WHEAT"]),("Gathering",["FAMILY","FRIENDS","DINNER","THANKS"])],
"christmas":[("Tree decorations",["LIGHTS","STAR","TINSEL","ORNAMENT"]),("Santa's trip",["SLEIGH","REINDEER","CHIMNEY","NORTH"]),("Wrapped up",["GIFT","BOX","BOW","PAPER"]),("Holiday treats",["COOKIE","COCOA","CANDY","GINGER"])],
"valentines":[("Valentine gifts",["ROSES","CANDY","CARD","FLOWERS"]),("Terms of affection",["DEAR","HONEY","SWEETIE","LOVE"]),("Heart shapes",["LOCKET","COOKIE","BALLOON","PENDANT"]),("Date night",["DINNER","MOVIE","DANCE","MUSIC"])],
"st_patricks":[("Going green",["CLOVER","EMERALD","LIME","MOSS"]),("Lucky things",["HORSESHOE","RABBIT","PENNY","CHARM"]),("Irish symbols",["HARP","SHAMROCK","GREEN","CELTIC"]),("Parade day",["MARCH","FLOAT","MUSIC","CROWD"])],
"halloween":[("Costumes",["WITCH","GHOST","VAMPIRE","PIRATE"]),("Trick-or-treat",["CANDY","BAG","DOORBELL","PORCH"]),("Spooky places",["CRYPT","ATTIC","CELLAR","GRAVEYARD"]),("Pumpkin carving",["KNIFE","SEEDS","CANDLE","FACE"])],
}

# Word Weave boards use a 6x6 grid. Answers are arranged as adjacent paths;
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
    ("Autumn days", ["MAPLE","FALL","RUST","COZY","ACORN","AUTUMN","CIDER","PIE"], 5),
    ("Halloween night", ["GHOST","MASK","BATS","DARK","CANDY","SPOOKY","WITCH","BOO"], 5),
    ("Thanksgiving table", ["GRAVY","YAMS","CORN","OVEN","PLATE","DINNER","FEAST","HAM"], 5),
    ("Christmas morning", ["HOLLY","STAR","GIFT","BELL","ELVES","TINSEL","SANTA","JOY"], 5),
    ("New Year's Eve", ["CLOCK","YEAR","BALL","KISS","PARTY","CHEERS","SPARK","EVE"], 5),
    ("Valentine's Day", ["HEART","LOVE","ROSE","DATE","CANDY","CUPIDS","SWEET","HUG"], 5),
    ("Easter morning", ["BUNNY","EGGS","HUNT","NEST","JELLY","SPRING","CHICK","DYE"], 5),
    ("Summer vacation", ["BEACH","HEAT","SWIM","SAND","SUNNY","SUMMER","WAVES","SUN"], 5),
    ("Rainy day", ["CLOUD","RAIN","BOOT","DROP","STORM","SHOWER","MISTY","WET"], 5),
    ("Thunderstorm", ["LIGHT","RAIN","WIND","DARK","CLOUD","STORMS","FLASH","SKY"], 5),
    ("Rainbow colors", ["COLOR","ARCH","RAIN","GLOW","PRISM","BRIGHT","CLOUD","SKY"], 5),
    ("Mountain hike", ["PEAKS","ROCK","HIKE","COLD","TRAIL","SUMMIT","CLIFF","MAP"], 5),
    ("Desert trip", ["CACTI","SAND","HEAT","DUNE","OASIS","DESERT","CAMEL","SUN"], 5),
    ("Along the river", ["WATER","FLOW","BANK","RAFT","CREEK","STREAM","REEDS","DAM"], 5),
    ("At the lake", ["DOCKS","BOAT","FISH","SWIM","WATER","ISLAND","CABIN","OAR"], 5),
    ("City streets", ["BLOCK","TAXI","ROAD","SIGN","LIGHT","STREET","PLAZA","BUS"], 5),
    ("At the airport", ["PLANE","GATE","BAGS","TAXI","PILOT","FLIGHT","TOWER","JET"], 5),
    ("At the beach", ["SHELL","SAND","WAVE","TIDE","OCEAN","COASTS","BOARD","SEA"], 5),
    ("Fishing trip", ["HOOKS","BAIT","BOAT","LINE","TROUT","ANGLER","REELS","ROD"], 5),
    ("Picnic time", ["GRAPE","PARK","FOOD","BOWL","BREAD","PICNIC","APPLE","ANT"], 5),
    ("Birthday party", ["CAKES","GIFT","CARD","WISH","CANDY","CANDLE","PARTY","HAT"], 5),
    ("Wedding day", ["BRIDE","RING","VOWS","CAKE","DANCE","GROOMS","WHITE","JOY"], 5),
    ("At the circus", ["CLOWN","RING","TENT","SHOW","TRICK","CIRCUS","HORSE","FUN"], 5),
    ("At the zoo", ["TIGER","BEAR","LION","CAGE","ZEBRA","MONKEY","OTTER","APE"], 5),
    ("Safari", ["ZEBRA","LION","JEEP","WILD","RHINO","SAFARI","HYENA","MAP"], 5),
    ("Bird watching", ["ROBIN","WING","NEST","SONG","EAGLE","BIRDIE","HERON","OWL"], 5),
    ("Butterfly garden", ["WINGS","PINK","BLUE","REST","BLOOM","GARDEN","PETAL","BUG"], 5),
    ("Dog park", ["LEASH","BARK","BALL","WALK","TREAT","CANINE","FETCH","DOG"], 5),
    ("Aquarium", ["SHARK","TANK","FISH","REEF","CORAL","MARINE","WHALE","EEL"], 5),
    ("Art class", ["PAINT","DRAW","CLAY","LINE","BRUSH","ARTIST","COLOR","INK"], 5),
    ("Dance class", ["STEPS","TURN","LEAP","BEAT","MUSIC","DANCER","STAGE","TAP"], 5),
    ("Book club", ["NOVEL","READ","PAGE","PLOT","STORY","AUTHOR","TITLE","INK"], 5),
    ("Photography", ["PHOTO","LENS","SHOT","ZOOM","FLASH","CAMERA","IMAGE","PIC"], 5),
    ("Tool box", ["DRILL","NAIL","BOLT","FILE","TOOLS","HAMMER","LEVEL","SAW"], 5),
    ("Train station", ["TRACK","RAIL","SEAT","STOP","DEPOT","ENGINE","TRAIN","CAR"], 5),
    ("On a bicycle", ["PEDAL","BIKE","GEAR","ROAD","CHAIN","CYCLER","BRAKE","AIR"], 5),
    ("Pool day", ["FLOAT","DIVE","LANE","DEEP","WATER","SPLASH","TOWEL","SUN"], 5),
    ("Bee hive", ["HONEY","BUZZ","WING","HIVE","QUEEN","WORKER","SWARM","BEE"], 5),
    ("Cat nap", ["KITTY","PURR","PAWS","NAPS","WHISK","FELINE","CLAWS","CAT"], 5),
    ("Dinosaur dig", ["BONES","BONE","ROCK","DIGS","TEETH","FOSSIL","CLAWS","EGG"], 5),
    ("Robot lab", ["ROBOT","CODE","WIRE","GEAR","METAL","DROIDS","LASER","BOT"], 5),
    ("Science lab", ["FLASK","ATOM","TEST","DATA","LASER","BEAKER","PROBE","LAB"], 5),
    ("Music room", ["PIANO","NOTE","DRUM","SONG","SOUND","GUITAR","VOICE","JAM"], 5),
    ("Library visit", ["BOOKS","READ","PAGE","DESK","STORY","NOVELS","SHELF","INK"], 5),
    ("Writing desk", ["PAPER","PENS","NOTE","WORD","DRAFT","PENCIL","ERASE","INK"], 5),
    ("Painting", ["BRUSH","BLUE","TONE","LINE","PAINT","CANVAS","COLOR","ART"], 5),
    ("Pottery", ["GLAZE","KILN","BOWL","MUGS","SHAPE","POTTER","CLAYS","ART"], 5),
    ("Woodworking", ["BOARD","SAWS","NAIL","SAND","TOOLS","CARVER","GRAIN","OAK"], 5),
    ("Garage work", ["MOTOR","TIRE","JACK","OILS","TOOLS","GARAGE","LEVEL","CAR"], 5),
    ("Car wash", ["SOAPY","WASH","HOSE","WAXY","SHINE","RINSED","TOWEL","CAR"], 5),
    ("Pizza night", ["SLICE","OVEN","HERB","MEAT","SAUCE","PIZZAS","DOUGH","PIE"], 5),
    ("Ice cream shop", ["SCOOP","CONE","MINT","COLD","CREAM","SUNDAE","FUDGE","CUP"], 5),
    ("Candy shop", ["SWEET","MINT","GUMS","SOUR","FUDGE","SUGARY","TAFFY","POP"], 5),
    ("Tea time", ["HONEY","MINT","CUPS","WARM","LEMON","TEAPOT","SUGAR","TEA"], 5),
    ("Farmers market", ["PEACH","CORN","BEAN","KALE","APPLE","MARKET","MELON","EGG"], 5),
    ("Grocery aisle", ["PASTA","RICE","SOUP","CANS","BREAD","GROCER","FRUIT","TEA"], 5),
    ("Taco night", ["SALSA","BEEF","CORN","LIME","CHILI","TACOES","ONION","DIP"], 5),
    ("Burger joint", ["PATTY","BUNS","MELT","SODA","SAUCE","BURGER","ONION","POP"], 5),
    ("Soup season", ["BROTH","HERB","BOWL","WARM","ONION","SIMMER","SPICE","POT"], 5),
    ("Fruit bowl", ["MANGO","PEAR","PLUM","KIWI","GRAPE","BANANA","PEACH","FIG"], 5),
    ("Vegetable patch", ["ONION","KALE","BEET","PEAS","CHARD","GARDEN","ROOTS","YAM"], 5),
    ("Morning routine", ["BRUSH","WASH","SOAP","COMB","ALARM","AWAKEN","TOWEL","DAY"], 5),
    ("Bedtime", ["SHEET","BOOK","LAMP","YAWN","DREAM","SLEEPY","BLANK","BED"], 5),
    ("Laundry day", ["SHIRT","WASH","SOAP","FOLD","DRYER","LAUNDR","SOCKS","BIN"], 5),
    ("Cleaning day", ["BROOM","MOPS","DUST","WIPE","SPRAY","POLISH","CLOTH","RAG"], 5),
    ("Home office", ["MOUSE","DESK","CALL","NOTE","CHAIR","OFFICE","PAPER","PEN"], 5),
    ("Movie theater", ["FILMS","SEAT","REEL","SHOW","CANDY","MOVIES","STAGE","POP"], 5),
    ("Arcade", ["TOKEN","GAME","PLAY","JOYS","LASER","ARCADE","PRIZE","PIN"], 5),
    ("Bowling alley", ["LANES","BALL","PINS","ROLL","SCORE","BOWLER","SHOES","FUN"], 5),
    ("Baseball game", ["PITCH","BATS","BASE","RUNS","GLOVE","INNING","FIELD","FAN"], 5),
    ("Football game", ["FIELD","PASS","KICK","TEAM","SCORE","PLAYER","COACH","WIN"], 5),
    ("Basketball court", ["HOOPS","BALL","PASS","SHOT","COURT","BASKET","SCORE","WIN"], 5),
    ("Soccer match", ["GOALS","BALL","PASS","KICK","FIELD","SOCCER","COACH","WIN"], 5),
    ("Hockey rink", ["PUCKS","ICER","GOAL","RINK","STICK","HOCKEY","SKATE","WIN"], 5),
    ("Tennis match", ["SERVE","BALL","SETS","LOVE","COURT","TENNIS","RALLY","ACE"], 5),
    ("Golf course", ["GREEN","BALL","CLUB","HOLE","DRIVE","GOLFER","CADDY","PAR"], 5),
    ("Ski lodge", ["SLOPE","SNOW","BOOT","COLD","LODGE","SKIERS","CABIN","SKI"], 5),
    ("Snow day", ["FLAKE","SLED","SNOW","COLD","GLOVE","WINTER","BOOTS","ICE"], 5),
    ("Fall harvest", ["APPLE","CORN","HAYS","LEAF","GOURD","AUTUMN","WHEAT","PIE"], 5),
    ("Orchard", ["APPLE","TREE","PEAR","PICK","FRUIT","GROVES","CRATE","BEE"], 5),
    ("Vineyard", ["GRAPE","VINE","CORK","CELL","CASKS","WINERY","PICKS","SUN"], 5),
    ("Flower shop", ["ROSES","VASE","STEM","IRIS","PETAL","FLORAL","TULIP","BUD"], 5),
    ("Camping gear", ["TENTS","ROPE","PACK","BOOT","TORCH","CAMPER","STOVE","MAP"], 5),
    ("Hiking trail", ["TRAIL","BOOT","PACK","ROCK","WATER","HIKERS","TREES","MAP"], 5),
    ("National park", ["TRAIL","BEAR","PINE","VIEW","RIVER","RANGER","LODGE","MAP"], 5),
    ("Waterfall", ["SPRAY","ROCK","POOL","DROP","WATER","FALLEN","MISTY","DAM"], 5),
    ("Cave exploring", ["CAVES","ROCK","DARK","LAMP","STONE","CAVERN","WINGS","MAP"], 5),
    ("Volcano", ["FIERY","DUST","ROCK","HEAT","MAGMA","CRATER","SMOKE","HOT"], 5),
    ("Arctic adventure", ["POLAR","SNOW","SEAL","COLD","IGLOO","ARCTIC","WHALE","ICE"], 5),
    ("Tropical island", ["PALMS","SAND","WAVE","WARM","MANGO","ISLAND","BEACH","SEA"], 5),
    ("Jungle trek", ["VINES","FROG","BIRD","RAIN","TIGER","JUNGLE","LEAFY","MAP"], 5),
    ("Pond life", ["FROGS","REED","FISH","LILY","WATER","MARSHY","DUCKS","BUG"], 5),
    ("Night sky", ["STARS","MOON","DARK","GLOW","COMET","COSMOS","ORBIT","SKY"], 5),
    ("Sunrise", ["LIGHT","DAWN","PINK","GOLD","CLOUD","ORANGE","BIRDS","DAY"], 5),
    ("Sunset", ["AMBER","DUSK","PINK","GLOW","CLOUD","SUNSET","NIGHT","SKY"], 5),
    ("Moonlight", ["MOONS","GLOW","DARK","BEAM","NIGHT","SILVER","STARS","SKY"], 5),
    ("Stargazing", ["STARS","DARK","MOON","VIEW","COMET","COSMOS","ORBIT","SKY"], 5),
    ("Space station", ["EARTH","DOCK","CREW","ZERO","ORBIT","SPACER","SOLAR","LAB"], 5),
    ("Rocket launch", ["FLAME","FUEL","CREW","FIRE","BOOST","LAUNCH","SMOKE","PAD"], 5),
    ("Forest animals", ["MOOSE","BEAR","DEER","WOLF","OTTER","RABBIT","FOXES","OWL"], 5),
    ("Ocean animals", ["WHALE","SEAL","CRAB","TUNA","SHARK","DOLPHI","SQUID","EEL"], 5),
    ("Backyard birds", ["ROBIN","DOVE","WREN","CROW","FINCH","PARROT","HERON","OWL"], 5),
    ("Garden flowers", ["ROSES","IRIS","LILY","MUMS","TULIP","ORCHID","DAISY","BUD"], 5),
    ("Fresh herbs", ["BASIL","DILL","MINT","SAGE","THYME","PARSLE","CHIVE","BAY"], 5),
    ("Trees and leaves", ["MAPLE","OAKS","ELMS","PINE","BIRCH","FOREST","CEDAR","ASH"], 5),
    ("Mountain life", ["GOATS","BEAR","PINE","ROCK","EAGLE","SUMMIT","TRAIL","ELK"], 5),
    ("Desert life", ["CACTI","SAND","DUNE","HEAT","CAMEL","DESERT","AGAVE","SUN"], 5),
    ("Wetlands", ["REEDS","FROG","POND","MUDS","HERON","MARSHY","SEDGE","BOG"], 5),
    ("Coral reef", ["CORAL","REEF","FISH","WAVE","SHARK","MARINE","SQUID","SEA"], 5),
    ("Kitchen tools", ["KNIFE","FORK","BOWL","OVEN","SPOON","GRATER","PLATE","PAN"], 5),
    ("Baking day", ["FLOUR","EGGS","MILK","OVEN","YEAST","BAKING","SUGAR","PIE"], 5),
    ("Pasta dinner", ["PASTA","BEEF","HERB","BOIL","SAUCE","NOODLE","ONION","POT"], 5),
    ("Salad bowl", ["LETTU","KALE","BEET","CORN","OLIVE","SALADS","ONION","PEA"], 5),
    ("Sandwich shop", ["BREAD","MEAT","MAYO","ROLL","BACON","HOAGIE","ONION","HAM"], 5),
    ("Breakfast cafe", ["TOAST","EGGS","OATS","MILK","BACON","WAFFLE","HONEY","TEA"], 5),
    ("Dessert cart", ["CAKES","TART","PIES","MINT","FUDGE","SWEETS","CREAM","POP"], 5),
    ("Spice rack", ["CHILI","DILL","SALT","SAGE","THYME","SPICES","CUMIN","BAY"], 5),
    ("School supplies", ["PAPER","BOOK","RULR","PENS","CHALK","PENCIL","ERASE","INK"], 5),
    ("Classroom", ["DESKS","BOOK","MATH","BELL","CHALK","TEACHR","PAPER","PEN"], 5),
    ("Playground", ["SWING","SLID","BALL","ROPE","BENCH","RECESS","GRASS","TAG"], 5),
    ("Workshop", ["DRILL","NAIL","BOLT","FILE","HAMMR","HAMMER","LEVEL","SAW"], 5),
    ("Sewing basket", ["YARNS","PINS","WOOL","SEAM","NEEDL","SEWING","CLOTH","HEM"], 5),
    ("Craft table", ["PASTE","YARN","CLAY","TAPE","PAINT","CRAFTS","PAPER","INK"], 5),
    ("Computer desk", ["MOUSE","KEYS","CODE","DATA","TRACK","LAPTOP","CABLE","APP"], 5),
    ("Phone screen", ["TOUCH","CALL","TEXT","RING","PHOTO","MOBILE","ALERT","APP"], 5),
    ("Video games", ["QUEST","PLAY","BOSS","MODE","SCORE","GAMING","BONUS","WIN"], 5),
    ("Board games", ["DICES","CARD","MOVE","TURN","TOKEN","GAMING","BOARD","FUN"], 5),
    ("Card games", ["HEART","DECK","HAND","SUIT","TRICK","DEALER","SPADE","ACE"], 5),
    ("Chess board", ["QUEEN","KING","ROOK","PAWN","CHECK","KNIGHT","BOARD","WIN"], 5),
    ("Running race", ["TRACK","PACE","MILE","FAST","SHOES","RUNNER","START","WIN"], 5),
    ("Gym workout", ["SQUAT","LIFT","REPS","SETS","BENCH","FITNES","WEIGH","GYM"], 5),
    ("Yoga class", ["POSES","CALM","MATS","BEND","LOTUS","YOGINI","FLOWS","ZEN"], 5),
    ("Swimming", ["FLOAT","DIVE","LANE","KICK","WATER","SWIMMR","STROK","LAP"], 5),
    ("Sailing", ["SAILS","WIND","MAST","DECK","OCEAN","SAILOR","ANCHR","SEA"], 5),
    ("Kayaking", ["KAYAK","BOAT","WAVE","RAPD","PADDL","KAYAKS","VESTS","OAR"], 5),
    ("Horse riding", ["HORSE","REIN","BOOT","TROT","TROTS","SADDLE","TRAIL","HAY"], 5),
    ("Camping night", ["TENTS","FIRE","WOOD","DARK","STARS","CAMPER","TORCH","MAP"], 5),
    ("Cabin weekend", ["CABIN","WOOD","FIRE","LAKE","LODGE","CABINS","TRAIL","MUG"], 5),
    ("Hotel stay", ["HOTEL","ROOM","KEYS","BEDS","LOBBY","GUESTS","TOWEL","SPA"], 5),
    ("Cruise ship", ["OCEAN","DECK","PORT","WAVE","CABIN","CRUISE","SHORE","SEA"], 5),
    ("Subway ride", ["TRAIN","STOP","RAIL","CITY","METRO","SUBWAY","FARES","MAP"], 5),
    ("Bus trip", ["BUSES","STOP","SEAT","ROAD","ROUTE","TRAVEL","FARES","MAP"], 5),
    ("Roadside stop", ["MOTEL","ROAD","SIGN","EXIT","SNACK","TRAVEL","RADIO","GAS"], 5),
    ("Museum", ["PAINT","ARTS","HALL","TOUR","STATU","MUSEUM","GUIDE","ART"], 5),
    ("Theater stage", ["ACTOR","PLAY","ROLE","LINE","STAGE","THEATR","DRAMA","ACT"], 5),
    ("Concert", ["MUSIC","BAND","SONG","BEAT","STAGE","SINGER","CROWD","JAM"], 5),
    ("Festival", ["MUSIC","FOOD","TENT","SHOW","LIGHT","FESTIV","CROWD","FUN"], 5),
    ("Carnival", ["RIDES","GAME","TENT","SHOW","CANDY","CARNIV","PRIZE","FUN"], 5),
    ("County fair", ["RIDES","CORN","BARN","SHOW","WAGON","MIDWAY","HORSE","FUN"], 5),
    ("Fire station", ["TRUCK","HOSE","BELL","FIRE","ALARM","RESCUE","HOSES","AXE"], 5),
    ("Police station", ["BADGE","CALL","DESK","RADR","PATRL","OFFICR","SIREN","LAW"], 5),
    ("Hospital", ["NURSE","CARE","BEDS","HEAL","DOCTR","CLINIC","GAUZE","DOC"], 5),
    ("Dentist", ["TEETH","CARE","FLOS","RINS","SMILE","DENTAL","PASTE","DRL"], 5),
    ("Eye doctor", ["SIGHT","LENS","READ","TEST","GLASS","VISION","FRAME","EYE"], 5),
    ("Barber shop", ["HAIRC","COMB","CUTS","TRIM","BRUSH","BARBER","RAZOR","GEL"], 5),
    ("Weather station", ["CLOUD","RAIN","WIND","HAIL","RADAR","RADARS","STORM","FOG"], 5),
    ("News room", ["PRESS","NEWS","COPY","DESK","STORY","REPORT","PAPER","AIR"], 5),
    ("Radio studio", ["RADIO","TALK","SONG","MIKE","VOICE","STUDIO","MUSIC","AIR"], 5),
    ("Film set", ["ACTOR","TAKE","ROLE","SHOT","SCENE","CAMERA","LIGHT","CUT"], 5),
    ("Apple orchard", ["CIDER","TREE","PEAR","PICK","APPLE","GROVES","CRATE","BEE"], 5),
    ("Pumpkin patch", ["GOURD","VINE","SEED","FALL","PATCH","AUTUMN","WAGON","PIE"], 5),
    ("Berry picking", ["BERRY","BUSH","RIPE","PICK","SWEET","BASKET","FRUIT","JAM"], 5),
    ("Corn maze", ["STALK","CORN","PATH","TURN","MAIZE","PUZZLE","FIELD","MAP"], 5),
    ("Maple season", ["MAPLE","TREE","BARK","BOIL","SYRUP","SUGARY","STEAM","PAN"], 5),
    ("Greenhouse", ["PLANT","PANE","POTS","WARM","SEEDS","GROWER","SPROU","SUN"], 5),
    ("Rose garden", ["ROSES","THOR","BUDS","PINK","PETAL","GARDEN","BLOOM","BEE"], 5),
    ("Wildflowers", ["DAISY","BLUE","FERN","WILD","BLOOM","FLOWER","PETAL","BEE"], 5),
    ("Herb garden", ["BASIL","MINT","DILL","SAGE","THYME","GARDEN","CHIVE","BAY"], 5),
    ("Backyard garden", ["SPADE","SOIL","SEED","HOSE","PLANT","GARDEN","TULIP","BEE"], 5),
    ("Rock garden", ["STONE","SAND","MOSS","PATH","ROCKS","GARDEN","FERNS","SPA"], 5),
    ("Tree house", ["TREES","WOOD","ROPE","RUNG","CABIN","SECRET","LIMBS","FUN"], 5),
    ("Backyard campout", ["TENTS","FIRE","YARD","DARK","STARS","CAMPER","TORCH","FUN"], 5),
    ("Porch evening", ["CHAIR","SWAY","LAMP","DUSK","PORCH","BREEZE","DRINK","CAT"], 5),
    ("Front yard", ["GRASS","GATE","PATH","LAWN","HEDGE","GARDEN","POSTS","DOG"], 5),
    ("Neighborhood", ["HOUSE","ROAD","PARK","WALK","BLOCK","NEIGHB","LOCAL","BUS"], 5),
    ("Downtown", ["TOWER","ROAD","SHOP","CITY","PLAZA","STREET","HOTEL","CAB"], 5),
    ("Skyscrapers", ["TOWER","PANE","HIGH","CITY","STEEL","HEIGHT","ROOFS","CAB"], 5),
    ("City park", ["GRASS","POND","PATH","TREE","BENCH","GARDEN","SWING","DOG"], 5),
    ("Public library", ["BOOKS","DESK","READ","HUSH","SHELF","STACKS","NOVEL","PEN"], 5),
    ("Bookstore", ["NOVEL","SHOP","READ","PAGE","SHELF","AUTHOR","COVER","INK"], 5),
    ("Comic shop", ["COMIC","HERO","BOOK","PAGE","CARDS","ISSUES","COVER","INK"], 5),
    ("Toy store", ["DOLLS","GAME","BALL","BEAR","BLOCK","PUZZLE","TRAIN","TOP"], 5),
    ("Pet store", ["LEASH","FISH","BIRD","FOOD","TREAT","ANIMAL","CAGES","CAT"], 5),
    ("Hardware store", ["DRILL","NAIL","BOLT","TOOL","PAINT","LUMBER","LEVEL","SAW"], 5),
    ("Garden center", ["PLANT","SOIL","POTS","SEED","SHRUB","GARDEN","HOSES","BEE"], 5),
    ("Bakery counter", ["BREAD","CAKE","ROLL","TART","FLOUR","BAKERY","DONUT","PIE"], 5),
    ("Diner", ["GRILL","HASH","EGGS","MALT","PLATE","COFFEE","TOAST","PIE"], 5),
    ("Food truck", ["TACOS","FIRE","CORN","LIME","SAUCE","STREET","ONION","VAN"], 5),
    ("Sushi bar", ["SUSHI","RICE","TUNA","ROLL","ROLLS","SALMON","PONZU","TEA"], 5),
    ("Noodle shop", ["RAMEN","BOWL","BEEF","BOIL","BROTH","NOODLE","ONION","TEA"], 5),
    ("Barbecue", ["SMOKE","FIRE","MEAT","HEAT","SAUCE","COOKER","AROMA","BBQ"], 5),
    ("Cookout", ["BURGR","FIRE","CORN","YARD","SAUCE","COOKER","CHIPS","BBQ"], 5),
    ("Potluck", ["PLATE","DISH","FOOD","PASS","SALAD","DINNER","BREAD","PIE"], 5),
    ("Brunch", ["TOAST","EGGS","OATS","HASH","BACON","BRUNCH","HONEY","TEA"], 5),
    ("Pancake breakfast", ["STACK","EGGS","MILK","FLIP","SYRUP","BATTER","BERRY","PAN"], 5),
    ("Cookie baking", ["DOUGH","OVEN","CHIP","MIXR","SUGAR","COOKIE","FLOUR","PAN"], 5),
    ("Chocolate shop", ["COCOA","DARK","MINT","MILK","FUDGE","BONBON","SWEET","BOX"], 5),
    ("Donut shop", ["DONUT","ICED","CAKE","RING","JELLY","BAKERY","SUGAR","BOX"], 5),
    ("Farm stand", ["APPLE","CORN","BEET","KALE","FRESH","MARKET","PEACH","EGG"], 5),
    ("Dairy farm", ["DAIRY","COWS","BARN","BALE","CREAM","FARMER","CURDS","EGG"], 5),
    ("Chicken coop", ["HATCH","COOP","NEST","FEED","CHICK","FARMER","ROOST","EGG"], 5),
    ("Horse barn", ["HORSE","REIN","BALE","TACK","TROTS","STABLE","BRUSH","OAT"], 5),
    ("Sheep farm", ["SHEEP","WOOL","BARN","FOLD","FLOCK","FARMER","GRASS","HAY"], 5),
    ("Tractor shed", ["WAGON","SHED","FUEL","PLOW","FIELD","FARMER","WHEEL","HAY"], 5),
    ("Harvest market", ["APPLE","CORN","BEET","KALE","FRESH","MARKET","GOURD","PIE"], 5),
    ("Spring rain", ["CLOUD","RAIN","DROP","WARM","GREEN","SPRING","BLOOM","DAY"], 5),
    ("Summer heat", ["SUNNY","HEAT","SWIM","WARM","BEACH","SUMMER","WATER","FAN"], 5),
    ("Autumn leaves", ["MAPLE","FALL","LEAF","GOLD","BROWN","AUTUMN","ACORN","RED"], 5),
    ("First snow", ["FLAKE","COLD","SNOW","SOFT","WHITE","WINTER","GLOVE","ICE"], 5),
    ("Foggy morning", ["CLOUD","MIST","GRAY","COOL","FOGGY","COFFEE","LIGHT","DAY"], 5),
    ("Windy day", ["GUSTS","WIND","KITE","BLOW","CLOUD","BREEZE","LEAFY","AIR"], 5),
    ("Hail storm", ["STORM","HAIL","COLD","WIND","CLOUD","RADARS","ROOFS","SKY"], 5),
    ("Heat wave", ["SUNNY","HEAT","HAZE","WARM","SWEAT","SUMMER","WATER","FAN"], 5),
    ("Cold snap", ["FROST","COLD","SNOW","WIND","CHILL","WINTER","GLOVE","HAT"], 5),
    ("Beach sunrise", ["OCEAN","DAWN","SAND","GOLD","LIGHT","ORANGE","WAVES","SEA"], 5),
    ("Beach sunset", ["OCEAN","DUSK","SAND","GOLD","AMBER","SUNSET","WAVES","SEA"], 5),
    ("Tide pools", ["SHELL","TIDE","CRAB","POOL","CORAL","MARINE","ROCKS","SEA"], 5),
    ("Sand dunes", ["SANDY","DUNE","WIND","DRYB","GRASS","DESERT","BEACH","SUN"], 5),
    ("Lighthouse", ["LIGHT","BEAM","ROCK","WAVE","TOWER","BEACON","SHORE","SEA"], 5),
    ("Harbor", ["BOATS","DOCK","PORT","WAVE","BUOYS","HARBOR","CRANE","SEA"], 5),
    ("Marina", ["BOATS","DOCK","SAIL","WAVE","YACHT","MARINA","ROPEY","SEA"], 5),
    ("Pier walk", ["BOARD","WALK","WAVE","WIND","PIERS","COASTS","GULLS","SEA"], 5),
    ("Boardwalk", ["RIDES","WALK","FOOD","GAME","BEACH","COASTS","CANDY","SEA"], 5),
    ("Shell hunting", ["SHELL","SAND","TIDE","WALK","BEACH","SEARCH","CORAL","SEA"], 5),
    ("Surfing", ["BOARD","WAVE","RIDE","SWIM","OCEAN","SURFER","BEACH","SEA"], 5),
    ("Snorkeling", ["MASKS","FINS","REEF","SWIM","CORAL","MARINE","FISHY","SEA"], 5),
    ("Scuba diving", ["TANKS","FINS","REEF","DIVE","CORAL","OXYGEN","SHARK","SEA"], 5),
    ("Whale watching", ["WHALE","BOAT","TAIL","BLOW","OCEAN","MARINE","SHORE","SEA"], 5),
    ("Dolphin pod", ["DOLPH","WAVE","SWIM","LEAP","OCEAN","MARINE","CLICK","SEA"], 5),
    ("Sea turtles", ["TURTL","REEF","SWIM","SAND","OCEAN","MARINE","SHELL","SEA"], 5),
    ("Shark week", ["SHARK","TEET","FINS","SWIM","OCEAN","MARINE","TEETH","SEA"], 5),
    ("Deep sea", ["SQUID","DARK","FISH","COLD","OCEAN","MARINE","LIGHT","SEA"], 5),
    ("River rafting", ["RAPID","RAFT","WAVE","ROCK","RIVER","PADDLE","VESTS","OAR"], 5),
    ("Canoe trip", ["CANOE","LAKE","SEAT","CALM","WATER","PADDLE","SHORE","OAR"], 5),
    ("Creek walk", ["CREEK","ROCK","FROG","FLOW","WATER","STREAM","FERNS","MUD"], 5),
    ("Mountain stream", ["CREEK","COLD","ROCK","FLOW","WATER","STREAM","TROUT","ICE"], 5),
    ("Forest creek", ["CREEK","MOSS","FERN","FLOW","WATER","FOREST","TRAIL","OWL"], 5),
    ("Woodland pond", ["PONDS","FROG","DUCK","REED","WATER","FOREST","ALGAE","OWL"], 5),
    ("Alpine lake", ["LAKES","COLD","ROCK","BLUE","WATER","ALPINE","TRAIL","ELK"], 5),
    ("Mountain cabin", ["CABIN","WOOD","FIRE","COLD","LODGE","SUMMIT","TRAIL","ELK"], 5),
    ("Mountain snow", ["SNOWY","COLD","SNOW","WIND","PEAKS","SUMMIT","TRAIL","SKI"], 5),
    ("Mountain meadow", ["GRASS","FERN","DEER","WIND","BLOOM","MEADOW","TRAIL","ELK"], 5),
    ("Forest floor", ["MOSSY","FERN","LEAF","DARK","FUNGI","FOREST","ACORN","OWL"], 5),
    ("Pine forest", ["PINES","CONE","FERN","DARK","RESIN","FOREST","TRAIL","OWL"], 5),
    ("Redwood grove", ["GIANT","BARK","FERN","TALL","TRUNK","FOREST","TRAIL","OWL"], 5),
    ("Birch grove", ["BIRCH","BARK","FERN","PALE","TRUNK","FOREST","TRAIL","OWL"], 5),
    ("Mushroom hunt", ["FUNGI","MOSS","FERN","DAMP","SPORE","FOREST","TRAIL","OWL"], 5),
    ("Acorn season", ["ACORN","OAKS","LEAF","FALL","NUTTY","FOREST","SQUIR","OWL"], 5),
    ("Bird nest", ["NESTS","TWIG","EGGS","SOFT","CHICK","PARENT","PLUME","OWL"], 5),
    ("Duck pond", ["DUCKS","POND","REED","SWIM","WATER","MARSHY","ALGAE","EGG"], 5),
    ("Frog pond", ["FROGS","POND","REED","JUMP","WATER","MARSHY","ALGAE","BUG"], 5),
    ("Dragonflies", ["WINGS","POND","BLUE","DART","FLIES","MARSHY","REEDS","BUG"], 5),
    ("Fireflies", ["LIGHT","DUSK","GLOW","DARK","FLIES","SUMMER","GRASS","BUG"], 5),
    ("Ladybugs", ["SPOTS","LEAF","LADY","TINY","WINGS","GARDEN","PLANT","BUG"], 5),
    ("Ant colony", ["TRAIL","NEST","FOOD","LINE","QUEEN","COLONY","SCOUT","BUG"], 5),
    ("Spider web", ["EIGHT","SILK","LACE","TRAP","FLIES","WEAVER","STICK","BUG"], 5),
    ("Butterflies", ["WINGS","FLIT","PINK","BLUE","BLOOM","GARDEN","PETAL","BUG"], 5),
    ("Honey bees", ["HONEY","HIVE","BUZZ","WING","QUEEN","WORKER","SWEET","BEE"], 5),
    ("Bumblebees", ["FUZZY","HIVE","BUZZ","WING","QUEEN","WORKER","HONEY","BEE"], 5),
    ("Monarchs", ["WINGS","GOLD","BLAC","FLIT","BLOOM","GARDEN","PETAL","BUG"], 5),
    ("Songbirds", ["ROBIN","SONG","WING","NEST","FINCH","FOREST","PLUME","OWL"], 5),
    ("Owls at night", ["NIGHT","DARK","WING","HOOT","MOONS","FOREST","PLUME","OWL"], 5),
    ("Eagles", ["EAGLE","WING","NEST","SOAR","TALON","RAPTOR","PLUME","SKY"], 5),
    ("Hummingbirds", ["HOVER","WING","BILL","HOVE","SUGAR","GARDEN","BLOOM","BEE"], 5),
    ("Penguins", ["CHICK","COLD","SWIM","DIVE","WATER","COLONY","SNOWY","SEA"], 5),
    ("Polar bears", ["POLAR","SNOW","SWIM","COLD","WHITE","ARCTIC","CLAWS","ICE"], 5),
    ("Seals", ["SEALS","COLD","SWIM","DIVE","WATER","ARCTIC","WHALE","SEA"], 5),
    ("Elephants", ["TRUNK","EARS","HERD","WALK","TUSKS","SAFARI","GRASS","ZOO"], 5),
    ("Giraffes", ["TOWER","NECK","LEAF","TALL","SPOTS","SAFARI","GRASS","ZOO"], 5),
    ("Zebras", ["ZEBRA","HERD","MANE","BAND","STRIP","SAFARI","PLAIN","ZOO"], 5),
    ("Lions", ["LIONS","ROAR","MANE","HUNT","PRIDE","SAFARI","GRASS","ZOO"], 5),
    ("Tigers", ["TIGER","ROAR","BAND","HUNT","CLAWS","JUNGLE","GRASS","ZOO"], 5),
    ("Monkeys", ["VINES","TREE","VINE","PLAY","FRUIT","JUNGLE","MANGO","ZOO"], 5),
    ("Pandas", ["PANDA","CANE","BEAR","EATS","BLACK","FOREST","SHOOT","ZOO"], 5),
    ("Koalas", ["KOALA","TREE","LEAF","NAPS","SLEEP","FOREST","LEAFY","ZOO"], 5),
    ("Kangaroos", ["JUMPS","JUMP","TAIL","HOPS","GRASS","DESERT","YOUNG","ZOO"], 5),
    ("Meerkats", ["WATCH","SAND","DENS","LOOK","ALERT","DESERT","GROUP","ZOO"], 5),
    ("Otters", ["OTTER","SWIM","ROCK","PLAY","RIVER","MARINE","SHELL","SEA"], 5),
    ("Peacocks", ["PLUME","TAIL","BLUE","SHOW","PLUME","BIRDIE","GREEN","ZOO"], 5),
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
    from datetime import date
    holiday = holiday_for_date(day)
    if holiday in _HOLIDAY_WEAVES:
        clue, words, thread_index = _HOLIDAY_WEAVES[holiday]
        paths = _WEAVE_PATHS
        letters = [""] * 36
        answers = []
        for index, (word, path) in enumerate(zip(words, paths)):
            for cell_index, char in zip(path, word):
                letters[cell_index] = char
            answers.append({"word": word, "path": path, "thread": index == thread_index})
        return {"clue": clue, "rows": 6, "cols": 6, "letters": letters, "words": answers}
    # Preserve the released v0.3.3 mapping for existing dates. New dates use
    # theme-first rotation so all 300 themes appear before a layout repeats.
    if day < date(2026, 10, 6):
        board_index = day.toordinal() % 100
        theme_count = 21
        theme_index = board_index % theme_count
        variant = (board_index // theme_count) % 5
    else:
        theme_count = len(_WEAVE_SETS)
        cycle_index = (day - date(2026, 10, 6)).days
        theme_index = cycle_index % theme_count
        variant = (cycle_index // theme_count) % 5
    clue, words, thread_index = _WEAVE_SETS[theme_index]
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
    length = int(length)
    holiday = holiday_for_date(day)
    if holiday and length == 5:
        return _HOLIDAY_WORDS[holiday]
    words = WORD_PUZZLES.get(length, WORD_PUZZLES[5])
    from datetime import date
    if length == 5 and day < date(2026, 10, 6):
        words = words[:70]
        return words[(day.toordinal() * 17 + length * 31) % len(words)]
    cycle = (day - date(2026, 10, 6)).days if day >= date(2026, 10, 6) else day.toordinal()
    return words[(cycle * 17 + length * 31) % len(words)]

def word_lengths_for_date(day):
    return {length: word_for_date(day, length) for length in sorted(WORD_PUZZLES)}

def groups_for_date(day):
    holiday = holiday_for_date(day)
    if holiday in _HOLIDAY_GROUPS:
        return [{"label": label, "words": words} for label, words in _HOLIDAY_GROUPS[holiday]]
    # Keep every released date stable. Expanded content begins on 2026-10-06.
    from datetime import date
    if day < date(2026, 10, 6):
        return _LEGACY_GROUP_PUZZLES[day.toordinal() % len(_LEGACY_GROUP_PUZZLES)]
    return GROUP_PUZZLES[(day - date(2026, 10, 6)).days % len(GROUP_PUZZLES)]
