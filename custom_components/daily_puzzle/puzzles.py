from __future__ import annotations

from .const import DEFAULT_ENABLED_GAMES

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


# Build a diversified 300-board Four of a Kind rotation from the authored
# category groups. Index sets are prevalidated to contain 16 unique answers.
_GROUP_SOURCE = [group for board in GROUP_PUZZLES for group in board]
_GROUP_BOARD_INDEXES = [[16,21,23,50],[11,17,30,44],[15,18,32,53],[9,22,27,52],[8,15,45,50],[19,20,22,49],[10,23,29,40],[0,7,18,37],[3,38,49,52],[7,21,24,50],[4,11,41,54],[2,21,31,48],[28,38,41,51],[15,18,21,32],[6,11,25,36],[19,22,49,52],[8,26,31,45],[11,12,17,54],[10,16,21,55],[19,22,41,52],[13,15,40,50],[9,14,43,44],[2,32,39,53],[17,27,28,46],[7,16,29,42],[12,46,49,51],[25,27,46,52],[2,29,48,55],[4,14,35,41],[8,18,45,55],[14,19,41,44],[0,23,26,29],[18,21,24,55],[12,14,17,43],[0,15,21,26],[3,20,22,49],[8,13,31,34],[17,28,43,54],[15,24,42,45],[19,20,22,41],[25,43,46,52],[0,21,26,55],[22,36,41,51],[0,26,29,39],[4,43,49,54],[7,8,26,53],[17,20,35,54],[8,26,45,55],[3,12,14,33],[26,32,39,45],[1,4,11,30],[0,42,47,53],[1,12,22,51],[0,5,10,47],[9,27,30,36],[0,34,37,55],[17,20,35,46],[15,24,26,53],[12,19,49,54],[0,15,18,53],[17,28,30,51],[5,7,10,32],[22,25,27,52],[5,7,10,48],[6,17,44,51],[4,9,46,51],[26,29,40,47],[17,22,27,52],[25,30,43,44],[5,18,24,31],[38,41,51,52],[8,13,31,50],[3,6,49,52],[7,24,29,34],[1,19,30,44],[16,26,39,45],[14,41,43,52],[18,31,37,48],[11,30,49,52],[13,26,47,48],[6,25,27,28],[27,33,36,46],[15,16,21,26],[36,41,43,46],[3,25,28,54],[31,32,42,45],[12,19,25,38],[2,24,31,45],[6,33,36,43],[2,23,32,45],[1,14,28,35],[0,37,50,55],[1,14,27,52],[31,40,50,53],[6,17,35,52],[0,37,47,50],[2,15,24,29],[21,34,48,55],[4,14,27,49],[0,15,21,34],[24,34,39,53],[9,22,28,51],[7,13,34,40],[22,33,43,52],[15,16,18,53],[17,19,46,52],[34,45,47,48],[16,29,31,50],[3,25,36,38],[2,8,23,37],[16,26,31,37],[12,14,25,27],[0,7,10,13],[4,9,22,27],[16,39,50,53],[2,5,8,23],[13,15,26,48],[14,19,28,33],[15,16,34,37],[1,28,38,51],[10,13,31,48],[2,5,31,40],[13,24,26,39],[11,25,36,46],[18,23,40,45],[14,25,27,52],[1,27,38,44],[13,16,23,42],[14,36,41,43],[0,2,5,7],[2,16,29,31],[6,19,41,52],[11,36,38,41],[0,15,18,21],[3,6,20,41],[18,24,37,39],[35,44,49,54],[13,24,26,47],[6,9,27,44],[7,13,16,34],[12,14,17,35],[0,2,7,45],[11,12,22,41],[2,7,32,37],[1,11,14,52],[0,5,31,42],[6,12,33,35],[23,29,32,34],[7,24,26,37],[9,28,38,43],[15,18,37,48],[4,11,14,25],[0,10,13,15],[9,36,38,51],[18,21,31,32],[0,2,5,15],[6,33,44,51],[13,23,26,32],[1,3,12,38],[11,25,38,52],[5,10,15,48],[19,25,44,54],[21,23,40,50],[6,19,28,33],[5,18,32,47],[11,30,36,49],[0,5,42,47],[20,33,43,46],[15,34,48,53],[3,14,17,44],[21,31,34,40],[30,43,49,52],[7,8,10,29],[11,22,25,52],[8,15,34,53],[4,11,22,33],[21,34,39,48],[12,35,46,49],[0,18,31,45],[17,35,36,38],[0,13,18,55],[1,12,19,30],[7,10,45,48],[17,36,51,54],[13,31,40,42],[9,11,14,36],[0,13,15,18],[15,37,48,50],[1,4,30,43],[8,13,18,31],[38,41,44,51],[16,23,29,34],[2,16,39,45],[25,27,36,46],[24,31,42,53],[6,11,17,44],[8,13,31,42],[11,22,44,49],[19,22,36,49],[21,31,32,50],[7,42,45,48],[4,19,30,41],[26,32,47,53],[1,28,30,51],[15,34,45,48],[3,20,25,54],[32,34,47,53],[11,30,41,52],[0,5,18,23],[9,30,36,51],[16,31,42,45],[11,17,46,52],[23,24,29,50],[2,15,37,48],[20,41,51,54],[13,15,34,48],[9,44,46,51],[13,32,39,42],[1,22,27,36],[15,26,32,45],[3,12,22,41],[8,15,26,53],[9,35,36,46],[13,16,39,42],[3,17,28,54],[21,32,42,47],[12,30,49,51],[2,5,15,16],[3,6,36,41],[0,5,26,55],[1,4,11,38],[2,16,23,45],[3,17,30,36],[1,3,6,28],[24,29,42,47],[0,10,13,31],[3,4,6,33],[0,26,39,45],[16,26,29,39],[6,19,44,49],[9,12,19,46],[7,18,29,40],[22,36,43,49],[0,2,5,39],[25,27,36,54],[18,39,45,48],[22,28,33,51],[0,50,53,55],[6,11,12,49],[40,42,47,53],[24,31,45,50],[25,28,43,54],[2,13,24,31],[25,38,43,44],[0,7,50,53],[25,30,36,51],[13,24,31,42],[14,35,41,44],[35,49,52,54],[7,32,34,45],[11,38,41,44],[8,21,42,47],[22,27,44,49],[24,34,37,47],[14,35,41,52],[10,47,48,53],[3,33,38,52],[0,2,13,23],[19,30,41,44],[16,26,29,47],[14,19,25,52],[8,21,31,42],[14,19,20,25],[13,39,48,50],[19,30,33,36],[15,16,42,45],[28,38,41,43],[32,39,50,53],[0,2,31,45],[23,26,37,48],[7,24,50,53],[3,17,22,52],[24,26,31,45],[12,22,35,41],[2,21,32,55],[19,41,44,46],[2,24,37,55],[1,28,30,43],[9,11,46,52],[13,15,48,50],[5,24,31,42],[6,12,41,51],[5,7,18,32],[19,20,22,33],[8,31,42,53],[6,12,43,49],[2,40,53,55],[27,44,49,54],[8,18,37,47],[1,12,35,38]]
GROUP_PUZZLES = [[_GROUP_SOURCE[index] for index in indexes] for indexes in _GROUP_BOARD_INDEXES]

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
    ("Burger joint", ["PATTY","BUNS","MELT","FRYS","SAUCE","BURGER","PICKL","POP"], 5),
    ("Soup season", ["BROTH","HERB","BOWL","WARM","ONION","SIMMER","SPICE","POT"], 5),
    ("Fruit bowl", ["MANGO","PEAR","PLUM","KIWI","GRAPE","BANANA","PEACH","FIG"], 5),
    ("Vegetable patch", ["ONION","KALE","BEET","PEAS","CHARD","GARDEN","CARRO","YAM"], 5),
    ("Morning routine", ["BRUSH","WASH","SOAP","COMB","COFFE","AWAKEN","TOWEL","DAY"], 5),
    ("Bedtime", ["SHEET","BOOK","LAMP","YAWN","DREAM","SLEEPY","PILLO","BED"], 5),
    ("Laundry day", ["SHIRT","WASH","SOAP","FOLD","DRYER","LAUNDR","SOCKS","BIN"], 5),
    ("Cleaning day", ["BROOM","MOPS","DUST","WIPE","SPRAY","CLEANR","CLOTH","RAG"], 5),
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
    ("Fall harvest", ["APPLE","CORN","HAYS","LEAF","GOURD","HARVST","WHEAT","PIE"], 5),
    ("Orchard", ["APPLE","TREE","PEAR","PICK","FRUIT","ORCHRD","BASKT","BEE"], 5),
    ("Vineyard", ["GRAPE","VINE","CORK","CELL","BARRE","VINEYR","HARVS","SUN"], 5),
    ("Flower shop", ["ROSES","VASE","STEM","BLOM","PETAL","FLORAL","TULIP","BUD"], 5),
    ("Camping gear", ["TENTS","ROPE","PACK","BOOT","TORCH","CAMPER","STOVE","MAP"], 5),
    ("Hiking trail", ["TRAIL","BOOT","PACK","ROCK","WATER","HIKERS","TREES","MAP"], 5),
    ("National park", ["TRAIL","BEAR","PINE","VIEW","RIVER","RANGER","LODGE","MAP"], 5),
    ("Waterfall", ["SPRAY","ROCK","POOL","DROP","WATER","FALLEN","MISTY","DAM"], 5),
    ("Cave exploring", ["CAVES","ROCK","DARK","LAMP","STONE","CAVERN","BATSY","MAP"], 5),
    ("Volcano", ["LAVAS","ASHY","ROCK","HEAT","MAGMA","CRATER","SMOKE","HOT"], 5),
    ("Arctic adventure", ["POLAR","SNOW","SEAL","COLD","IGLOO","ARCTIC","WHALE","ICE"], 5),
    ("Tropical island", ["PALMS","SAND","WAVE","WARM","COCON","ISLAND","BEACH","SEA"], 5),
    ("Jungle trek", ["VINES","FROG","BIRD","RAIN","TIGER","JUNGLE","LEAFY","MAP"], 5),
    ("Pond life", ["FROGS","REED","FISH","LILY","WATER","PONDLY","DUCKS","BUG"], 5),
    ("Night sky", ["STARS","MOON","DARK","GLOW","COMET","COSMOS","ORBIT","SKY"], 5),
    ("Sunrise", ["LIGHT","DAWN","PINK","GOLD","CLOUD","SUNRIS","BIRDS","DAY"], 5),
    ("Sunset", ["AMBER","DUSK","PINK","GLOW","CLOUD","SUNSET","NIGHT","SKY"], 5),
    ("Moonlight", ["MOONS","GLOW","DARK","BEAM","NIGHT","LUNARX","STARS","SKY"], 5),
    ("Stargazing", ["STARS","DARK","MOON","VIEW","COMET","COSMOS","ORBIT","SKY"], 5),
    ("Space station", ["EARTH","DOCK","CREW","ZERO","ORBIT","SPACER","SOLAR","LAB"], 5),
    ("Rocket launch", ["ROCKT","FUEL","CREW","FIRE","BOOST","LAUNCH","SMOKE","PAD"], 5),
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
    ("Sandwich shop", ["BREAD","MEAT","MAYO","ROLL","BACON","DELIXX","ONION","HAM"], 5),
    ("Breakfast cafe", ["TOAST","EGGS","OATS","MILK","BACON","WAFFLE","HONEY","TEA"], 5),
    ("Dessert cart", ["CAKES","TART","PIES","MINT","FUDGE","SWEETS","CREAM","POP"], 5),
    ("Spice rack", ["CHILI","DILL","SALT","SAGE","THYME","SPICES","CUMIN","BAY"], 5),
    ("School supplies", ["PAPER","BOOK","RULR","PENS","CHALK","PENCIL","ERASE","INK"], 5),
    ("Classroom", ["DESKS","BOOK","MATH","BELL","CHALK","TEACHR","PAPER","PEN"], 5),
    ("Playground", ["SWING","SLID","BALL","ROPE","BENCH","RECESS","GRASS","TAG"], 5),
    ("Workshop", ["DRILL","NAIL","BOLT","FILE","HAMMR","TOOLSX","LEVEL","SAW"], 5),
    ("Sewing basket", ["YARNS","PINS","WOOL","SEAM","NEEDL","SEWING","CLOTH","HEM"], 5),
    ("Craft table", ["GLUEX","YARN","CLAY","TAPE","PAINT","CRAFTS","PAPER","INK"], 5),
    ("Computer desk", ["MOUSE","KEYS","CODE","DATA","MOUSE","LAPTOP","CABLE","APP"], 5),
    ("Phone screen", ["TOUCH","CALL","TEXT","RING","PHOTO","MOBILE","ALERT","APP"], 5),
    ("Video games", ["QUEST","PLAY","BOSS","MODE","SCORE","GAMING","BONUS","WIN"], 5),
    ("Board games", ["DICES","CARD","MOVE","TURN","TOKEN","GAMING","BOARD","FUN"], 5),
    ("Card games", ["HEART","DECK","HAND","SUIT","TRICK","DEALER","SPADE","ACE"], 5),
    ("Chess board", ["QUEEN","KING","ROOK","PAWN","CHECK","CHESSX","BOARD","WIN"], 5),
    ("Running race", ["TRACK","PACE","MILE","FAST","SHOES","RUNNER","START","WIN"], 5),
    ("Gym workout", ["SQUAT","LIFT","REPS","SETS","BENCH","FITNES","WEIGH","GYM"], 5),
    ("Yoga class", ["POSES","CALM","MATS","BEND","POSES","YOGINI","STRET","ZEN"], 5),
    ("Swimming", ["FLOAT","DIVE","LANE","KICK","WATER","SWIMMR","STROK","LAP"], 5),
    ("Sailing", ["SAILS","WIND","MAST","DECK","OCEAN","SAILOR","ANCHR","SEA"], 5),
    ("Kayaking", ["KAYAK","BOAT","WAVE","RAPD","PADDL","KAYAKS","VESTS","OAR"], 5),
    ("Horse riding", ["HORSE","REIN","BOOT","TROT","SADDL","RIDERX","TRAIL","HAY"], 5),
    ("Camping night", ["TENTS","FIRE","WOOD","DARK","STARS","CAMPER","TORCH","MAP"], 5),
    ("Cabin weekend", ["CABIN","WOOD","FIRE","LAKE","LODGE","COZYXX","TRAIL","MUG"], 5),
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
    ("County fair", ["RIDES","CORN","BARN","SHOW","TRACT","FAIRXX","HORSE","FUN"], 5),
    ("Fire station", ["TRUCK","HOSE","BELL","FIRE","ALARM","RESCUE","HOSES","AXE"], 5),
    ("Police station", ["BADGE","CALL","DESK","RADR","PATRL","OFFICR","SIREN","LAW"], 5),
    ("Hospital", ["NURSE","CARE","BEDS","HEAL","DOCTR","CLINIC","GAUZE","ERX"], 5),
    ("Dentist", ["TEETH","CARE","FLOS","RINS","SMILE","DENTAL","PASTE","DRL"], 5),
    ("Eye doctor", ["SIGHT","LENS","READ","TEST","GLASS","VISION","FRAME","EYE"], 5),
    ("Barber shop", ["HAIRC","COMB","CUTS","TRIM","BRUSH","BARBER","RAZOR","GEL"], 5),
    ("Weather station", ["CLOUD","RAIN","WIND","HAIL","RADAR","WEATHR","STORM","FOG"], 5),
    ("News room", ["PRESS","NEWS","COPY","DESK","STORY","REPORT","PAPER","TVX"], 5),
    ("Radio studio", ["RADIO","TALK","SONG","MIKE","VOICE","STUDIO","MUSIC","FMX"], 5),
    ("Film set", ["ACTOR","TAKE","ROLE","SHOT","SCENE","CAMERA","LIGHT","CUT"], 5),
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
    # Theme-first rotation: every authored theme is used once before any theme
    # repeats with another board orientation. Layout is deliberately secondary
    # so consecutive days are driven by content rather than shuffled geometry.
    theme_count = len(_WEAVE_SETS)
    cycle_index = day.toordinal()
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
    words = WORD_PUZZLES.get(int(length), WORD_PUZZLES[5])
    # Give every length its own stable daily answer rather than the same list offset.
    return words[(day.toordinal() * 17 + int(length) * 31) % len(words)]

def word_lengths_for_date(day):
    return {length: word_for_date(day, length) for length in sorted(WORD_PUZZLES)}

def groups_for_date(day):
    return GROUP_PUZZLES[day.toordinal() % len(GROUP_PUZZLES)]
