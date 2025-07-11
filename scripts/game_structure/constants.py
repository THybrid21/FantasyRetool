import ujson

BIOME_TYPES = ["Forest", "Plains", "Mountainous", "Beach", "Wetlands", "Desert"]

SEASONS = ["Newleaf", "Greenleaf", "Leaf-fall", "Leaf-bare"]
SEASON_CALENDAR = [
    "Newleaf",
    "Newleaf",
    "Newleaf",
    "Greenleaf",
    "Greenleaf",
    "Greenleaf",
    "Leaf-fall",
    "Leaf-fall",
    "Leaf-fall",
    "Leaf-bare",
    "Leaf-bare",
    "Leaf-bare",
]

TEMPERAMENT_DICT = {
    "low_social": ["cunning", "proud", "bloodthirsty"],
    "mid_social": ["amiable", "stoic", "wary"],
    "high_social": ["gracious", "mellow", "logical"],
}

OUTSIDER_REPS = ("welcoming", "neutral", "hostile")
OTHER_CLAN_REPS = ("ally", "neutral", "hostile")

INJURY_GROUPS = {
    "battle_injury": [
        "claw-wound",
        "mangled leg",
        "mangled tail",
        "torn pelt",
        "cat bite",
    ],
    "minor_injury": ["sprain", "sore", "bruises", "scrapes"],
    "blunt_force_injury": ["broken bone", "broken back", "head damage", "broken jaw"],
    "hot_injury": ["heat exhaustion", "heat stroke", "dehydrated"],
    "cold_injury": ["shivering", "frostbite"],
    "big_bite_injury": [
        "bite-wound",
        "broken bone",
        "torn pelt",
        "mangled leg",
        "mangled tail",
    ],
    "small_bite_injury": ["bite-wound", "torn ear", "torn pelt", "scrapes"],
    "beak_bite": ["beak bite", "torn ear", "scrapes"],
    "rat_bite": ["rat bite", "torn ear", "torn pelt"],
    "sickness": ["greencough", "redcough", "whitecough", "yellowcough"],
}

EVENT_ALLOWED_CONDITIONS = [
    "tick bites",
    "claw-wound",
    "bite-wound",
    "cat bite",
    "beak bite",
    "snake bite",
    "quilled by a porcupine",
    "rat bite",
    "mangled leg",
    "mangled tail",
    "broken jaw",
    "broken bone",
    "sore",
    "bruises",
    "scrapes",
    "cracked pads",
    "small cut",
    "sprain",
    "bee sting",
    "joint pain",
    "dislocated joint",
    "torn pelt",
    "torn ear",
    "water in their lungs",
    "shivering",
    "frostbite",
    "burn",
    "severe burn",
    "shock",
    "dehydrated",
    "head damage",
    "damaged eyes",
    "broken back",
    "poisoned",
    "headache",
    "severe headache",
    "fleas",
    "seizure",
    "diarrhea",
    "running nose",
    "kittencough",
    "whitecough",
    "greencough",
    "yellowcough",
    "redcough",
    "carrionplace disease",
    "heat stroke",
    "heat exhaustion",
    "stomachache",
    "constant nightmares",
]

with open(f"resources/game_config.json", "r", encoding="utf-8") as read_file:
    CONFIG = ujson.loads(read_file.read())

with open("resources/placements.json", "r", encoding="utf-8") as read_file:
    LAYOUTS = ujson.loads(read_file.read())
