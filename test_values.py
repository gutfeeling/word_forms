# Test values must be in the form [(text_input, expected_output), (text_input, expected_output), ...]
test_values = [
    (
        "president",
        {
            "n": {
                "president",
                "presidentship",
                "presidencies",
                "presidency",
                "presidentships",
                "presidents",
            },
            "r": {"presidentially"},
            "a": {"presidential"},
            "v": {"presiding", "presides", "preside", "presided"},
        },
    ),
    (
        "elect",
        {
            "n": {
                "elector",
                "elects",
                "electors",
                "elective",
                "electorates",
                "elect",
                "electives",
                "elections",
                "electorate",
                "eligibility",
                "election",
                "eligibilities",
            },
            "r": set(),
            "a": {"elect", "electoral", "elective", "eligible"},
            "v": {"elect", "elects", "electing", "elected"},
        },
    ),
    (
        "running",
        {
            "n": {
                "runninesses",
                "runnings",
                "runs",
                "running",
                "runniness",
                "runners",
                "runner",
                "run",
            },
            "a": {"running", "runny"},
            "v": {"running", "ran", "runs", "run"},
            "r": set(),
        },
    ),
    (
        "run",
        {
            "n": {
                "runninesses",
                "runnings",
                "runs",
                "running",
                "runniness",
                "runners",
                "runner",
                "run",
            },
            "a": {"running", "runny"},
            "v": {"running", "ran", "runs", "run"},
            "r": set(),
        },
    ),
    (
        "operations",
        {
            "n": {
                "operators",
                "operations",
                "operation",
                "operative",
                "operator",
                "operatives",
            },
            "a": {"operant", "operative"},
            "v": {"operated", "operating", "operate", "operates"},
            "r": {"operatively"},
        },
    ),
    (
        "operate",
        {
            "n": {
                "operators",
                "operations",
                "operation",
                "operative",
                "operator",
                "operatives",
            },
            "a": {"operant", "operative"},
            "v": {"operated", "operating", "operate", "operates"},
            "r": {"operatively"},
        },
    ),
    (
        "invest",
        {
            "n": {
                "investitures",
                "investors",
                "investiture",
                "investor",
                "investments",
                "investings",
                "investment",
                "investing",
            },
            "a": set(),
            "v": {"invested", "invests", "invest", "investing"},
            "r": set(),
        },
    ),
    (
        "investments",
        {
            "n": {
                "investitures",
                "investors",
                "investiture",
                "investor",
                "investments",
                "investings",
                "investment",
                "investing",
            },
            "a": set(),
            "v": {"invested", "invests", "invest", "investing"},
            "r": set(),
        },
    ),
    (
        "conjugation",
        {
            "n": {"conjugate", "conjugation", "conjugates", "conjugations"},
            "a": {"conjugate"},
            "v": {"conjugating", "conjugated", "conjugate", "conjugates"},
            "r": set(),
        },
    ),
    (
        "do",
        {
            "n": {"does", "doer", "doers", "do"},
            "a": set(),
            "v": {
                "doing",
                "don't",
                "does",
                "didn't",
                "do",
                "doesn't",
                "done",
                "did",
            },
            "r": set(),
        },
    ),
    (
        "word",
        {
            "n": {"words", "word", "wordings", "wording"},
            "a": set(),
            "v": {"words", "word", "worded", "wording"},
            "r": set(),
        },
    ),
    (
        "love",
        {
            "a": {"lovable", "loveable"},
            "n": {"love", "lover", "lovers", "loves"},
            "r": set(),
            "v": {"love", "loved", "loves", "loving"},
        },
    ),
    (
        "word",
        {
            "n": {"words", "word", "wordings", "wording"},
            "a": set(),
            "v": {"words", "word", "worded", "wording"},
            "r": set(),
        },
    ),
    (
        "verb",
        {
            "n": {"verbs", "verb"},
            "a": {"verbal"},
            "v": {"verbifying", "verbified", "verbify", "verbifies"},
            "r": {"verbally"},
        },
    ),
    (
        "genetic",
        {
            "n": {"geneticist", "genetics", "geneticists", "genes", "gene"},
            "a": {"genic", "genetic", "genetical"},
            "v": set(),
            "r": {"genetically"},
        },
    ),
    (
        "politician",
        {
            "r": {"politically"},
            "a": {"political"},
            "n": {"politician", "politicians", "politics"},
            "v": set(),
        },
    ),
    (
        "death",
        {
            "n": {"death", "dying", "deaths", "die", "dyings", "dice"},
            "a": {"dying", "deathly"},
            "v": {"died", "die", "dying", "dies"},
            "r": {"deathly"},
        },
    ),
    (
        "attitude",
        {
            "n": {"attitudes", "attitude"},
            "a": set(),
            "v": {
                "attitudinise",
                "attitudinized",
                "attitudinize",
                "attitudinizes",
                "attitudinizing",
            },
            "r": set(),
        },
    ),
    (
        "cheek",
        {
            "n": {"cheek", "cheekinesses", "cheeks", "cheekiness"},
            "a": {"cheeky"},
            "v": {"cheek", "cheeks", "cheeked", "cheeking"},
            "r": {"cheekily"},
        },
    ),
    (
        "world",
        {
            "n": {"worldliness", "world", "worldlinesses", "worlds"},
            "a": {"worldly", "world"},
            "v": set(),
            "r": set(),
        },
    ),
    ("lake", {"n": {"lake", "lakes"}, "a": set(), "v": set(), "r": set()}),
    (
        "guitar",
        {
            "n": {"guitarist", "guitarists", "guitar", "guitars"},
            "a": set(),
            "v": set(),
            "r": set(),
        },
    ),
    (
        "presence",
        {
            "n": {
                "presenter",
                "present",
                "presents",
                "presentness",
                "presenters",
                "presentnesses",
                "presentments",
                "presentations",
                "presences",
                "presence",
                "presentment",
                "presentation",
            },
            "a": {"present"},
            "v": {"present", "presents", "presenting", "presented"},
            "r": {"presently"},
        },
    ),
    (
        "enthusiasm",
        {
            "n": {"enthusiasm", "enthusiasms"},
            "a": {"enthusiastic"},
            "v": set(),
            "r": {"enthusiastically"},
        },
    ),
    (
        "organization",
        {
            "n": {"organizers", "organization", "organizations", "organizer"},
            "a": set(),
            "v": {"organize", "organized", "organizing", "organizes"},
            "r": set(),
        },
    ),
    (
        "player",
        {
            "n": {
                "plays",
                "playlet",
                "playings",
                "players",
                "playing",
                "playlets",
                "play",
                "player",
            },
            "a": set(),
            "v": {"plays", "play", "playing", "played"},
            "r": set(),
        },
    ),
    (
        "transportation",
        {
            "n": {
                "transporters",
                "transportation",
                "transportations",
                "transporter",
                "transport",
                "transports",
            },
            "a": set(),
            "v": {"transport", "transporting", "transports", "transported"},
            "r": set(),
        },
    ),
    (
        "television",
        {
            "n": {"televisions", "television"},
            "a": set(),
            "v": {"televising", "televise", "televises", "televised"},
            "r": set(),
        },
    ),
    (
        "cousin",
        {"n": {"cousins", "cousin"}, "a": {"cousinly"}, "v": set(), "r": set()},
    ),
    (
        "ability",
        {"n": {"abilities", "ability"}, "a": {"able"}, "v": set(), "r": {"ably"}},
    ),
    ("chapter", {"n": {"chapters", "chapter"}, "a": set(), "v": set(), "r": set()}),
    (
        "appearance",
        {
            "n": {
                "appearances",
                "apparitions",
                "appearance",
                "apparencies",
                "apparentness",
                "apparentnesses",
                "apparition",
                "apparency",
            },
            "a": {"apparent"},
            "v": {"appears", "appeared", "appear", "appearing"},
            "r": {"apparently"},
        },
    ),
    (
        "drawing",
        {
            "n": {
                "drawings",
                "drawers",
                "draws",
                "drawer",
                "drawees",
                "drawee",
                "draw",
                "drawing",
            },
            "a": set(),
            "v": {"draws", "drew", "drawn", "draw", "drawing"},
            "r": set(),
        },
    ),
    (
        "university",
        {"n": {"university", "universities"}, "a": set(), "v": set(), "r": set()},
    ),
    (
        "performance",
        {
            "n": {
                "performings",
                "performing",
                "performances",
                "performance",
                "performer",
                "performers",
            },
            "a": set(),
            "v": {"performs", "performing", "performed", "perform"},
            "r": set(),
        },
    ),
    ("revenue", {"n": {"revenue", "revenues"}, "a": set(), "v": set(), "r": set()}),
    # Some Verbs
    (
        "cling",
        {
            "n": {"cling", "clings"},
            "a": set(),
            "v": {"clung", "cling", "clinging", "clings"},
            "r": set(),
        },
    ),
    (
        "decrease",
        {
            "n": {"decrease", "decreases"},
            "a": set(),
            "v": {"decrease", "decreases", "decreased", "decreasing"},
            "r": set(),
        },
    ),
    (
        "wonder",
        {
            "n": {
                "wonder",
                "wonderment",
                "wonderments",
                "wonders",
                "wonderers",
                "wonderer",
            },
            "a": {"wondrous"},
            "v": {"wondering", "wonder", "wonders", "wondered"},
            "r": {"wondrous", "wondrously"},
        },
    ),
    (
        "rest",
        {
            "n": {"rest", "rests", "resters", "rester"},
            "a": set(),
            "v": {"rest", "rests", "resting", "rested"},
            "r": set(),
        },
    ),
    (
        "mutter",
        {
            "n": {
                "mutterer",
                "mutterers",
                "muttering",
                "mutter",
                "mutterings",
                "mutters",
            },
            "a": set(),
            "v": {"muttering", "muttered", "mutters", "mutter"},
            "r": set(),
        },
    ),
    (
        "implement",
        {
            "n": {"implementations", "implement", "implements", "implementation"},
            "a": {"implemental"},
            "v": {"implemented", "implement", "implements", "implementing"},
            "r": set(),
        },
    ),
    (
        "evolve",
        {
            "n": {"evolution", "evolutions"},
            "a": {"evolutionary"},
            "v": {"evolved", "evolve", "evolves", "evolving"},
            "r": {"evolutionarily"},
        },
    ),
    (
        "allocate",
        {
            "n": {"allocations", "allocators", "allocation", "allocator"},
            "a": {"allocable", "allocatable"},
            "v": {"allocating", "allocates", "allocated", "allocate"},
            "r": set(),
        },
    ),
    (
        "flood",
        {
            "n": {"flood", "flooding", "floodings", "floods"},
            "a": set(),
            "v": {"flooding", "flooded", "flood", "floods"},
            "r": set(),
        },
    ),  # Should there be `flooded` in 'a' here?
    (
        "bow",
        {
            "n": {"bows", "bow"},
            "a": set(),
            "v": {"bows", "bowing", "bowed", "bow"},
            "r": set(),
        },
    ),
    (
        "advocate",
        {
            "n": {
                "advocates",
                "advocator",
                "advocacy",
                "advocacies",
                "advocators",
                "advocate",
            },
            "a": set(),
            "v": {"advocates", "advocating", "advocated", "advocate"},
            "r": set(),
        },
    ),
    (
        "divert",
        {
            "n": {"diversions", "diversionists", "diversionist", "diversion"},
            "a": {"diversionary"},
            "v": {"diverted", "diverts", "divert", "diverting"},
            "r": set(),
        },
    ),
    # Some adjectives
    (
        "sweet",
        {
            "n": {"sweetnesses", "sweets", "sweetness", "sweet"},
            "a": {"sweet"},
            "v": set(),
            "r": {"sweet", "sweetly"},
        },
    ),
    (
        "glossy",
        {
            "n": {"glossiness", "glossy", "glossies", "glossinesses"},
            "a": {"glossy"},
            "v": set(),
            "r": {"glossily"},
        },
    ),
    (
        "relevant",
        {
            "n": {"relevancies", "relevance", "relevancy", "relevances"},
            "a": {"relevant"},
            "v": set(),
            "r": {"relevantly"},
        },
    ),
    (
        "aloof",
        {"n": {"aloofnesses", "aloofness"}, "a": {"aloof"}, "v": set(), "r": {"aloof"}},
    ),
    (
        "therapeutic",
        {
            "n": {
                "therapists",
                "therapies",
                "therapy",
                "therapist",
                "therapeutic",
                "therapeutics",
            },
            "a": {"therapeutical", "therapeutic"},
            "v": set(),
            "r": {"therapeutically"},
        },
    ),
    (
        "obviously",
        {
            "n": {"obviousnesses", "obviousness"},
            "a": {"obvious"},
            "v": set(),
            "r": {"obviously"},
        },
    ),
    (
        "jumpy",
        {
            "n": {"jumpings", "jumpiness", "jumpinesses", "jump", "jumping", "jumps"},
            "a": {"jumpy"},
            "v": {"jump", "jumping", "jumped", "jumps"},
            "r": set(),
        },
    ),
    (
        "venomous",
        {"n": {"venom", "venoms"}, "a": {"venomous"}, "v": set(), "r": {"venomously"}},
    ),
    (
        "laughable",
        {
            "n": {"laugher", "laughs", "laughers", "laugh"},
            "a": {"laughable"},
            "v": {"laughing", "laughs", "laughed", "laugh"},
            "r": {"laughably"},
        },
    ),
    (
        "demonic",
        {
            "n": {"demons", "demon", "demonizations", "demonization"},
            "a": {"demonic"},
            "v": {"demonized", "demonizing", "demonizes", "demonize"},
            "r": set(),
        },
    ),
    (
        "knotty",
        {
            "n": {"knot", "knottiness", "knots", "knottinesses"},
            "a": {"knotty"},
            "v": {"knotted", "knotting", "knots", "knot"},
            "r": set(),
        },
    ),  # Is `knottinesses` a valid plural?
    (
        "little",
        {
            "n": {"little", "littlenesses", "littles", "littleness"},
            "a": {"little"},
            "v": set(),
            "r": {"little"},
        },
    ),  # Is `littlenesses` a valid plural?
    # "puzzling" and "overrated" should be checked
]