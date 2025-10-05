import random

def generate_alien_profiles(n):
    # Predefined lists of species and planets
    species_list = [
        "Zarnak", "Velorian", "Threxian", "Morbax", "Quorlan",
        "Xentari", "Dravari", "Nublith", "Krell", "Orryx",
        "Varnathi", "Skeel", "Tarnok", "Yllari", "Gorvax",
        "Elyndra", "Braxil", "Zenthari", "Ulthari", "Kryll"
    ]
    planet_list = [
        "Xebulon-5", "Velos", "Threxia", "Morbos", "Quorlia",
        "Xentar Prime", "Dravar IX", "Nublith Core", "Krellon", "Orryx Delta",
        "Varnath", "Skeelos", "Tarnok Minor", "Yllarion", "Gorvax Prime",
        "Elyndros", "Braxilion", "Zenthara", "Ulthar", "Kryllos"
    ]

    # Pool of possible items, with some flagged as banned
    item_list = [
        "passport", "fruit", "plasma cutter", "neurotoxin", "black crystal",
        "data chip", "translator", "energy cell", "medkit", "artifact",
        "quantum shard", "stasis pod", "gravity boots", "ion blaster", "holo scroll",
        "warp coil", "bio scanner", "fusion rod", "nano mist", "stellar map",
        "plasma grenade", "xeno relic", "cryogel", "dark matter vial", "antimatter core",
        "phase disruptor", "temporal beacon", "subspace key", "alien flora", "synthetic meat",
        "hologram projector", "reactor core", "space rations", "oxygen tank", "thermal cloak",
        "magnetic gloves", "laser scalpel", "biofoam", "shield emitter", "neural uplink",
        "xeno spores", "mind crystal", "telepathy enhancer", "gravity stabilizer", "warp stabilizer",
        "dimensional anchor", "psi amplifier", "plasma torch", "fusion battery", "stellar compass",
        "xeno script", "bio sample", "alien egg", "plasma vial", "dark crystal",
        "quantum lens", "ion cell", "reactive gel", "nano drone", "xeno tech",
        "psi crystal", "warp drive", "gravity lens", "bio injector", "plasma net",
        "neural dampener", "alien alloy", "stellar beacon", "fusion injector", "xeno mask",
        "temporal crystal", "subspace relay", "bio tracker", "gravity anchor", "plasma coil",
        "dark shard", "quantum drive", "ion stabilizer", "warp beacon", "psi disruptor",
        "xeno scanner", "bio helmet", "plasma blade", "fusion core", "stellar relic",
        "alien tome", "gravity chip", "nano shield", "psi emitter", "warp crystal",
        "neural interface", "plasma bomb", "bio enhancer", "stellar chart", "xeno compass",
        "fusion lens", "dark vial", "quantum crystal", "psi lens", "warp stabilizer"
    ]

    banned_items = {
        "neurotoxin", "black crystal", "plasma grenade", "dark matter vial", "antimatter core",
        "phase disruptor", "xeno spores", "mind crystal", "telepathy enhancer", "dimensional anchor",
        "psi amplifier", "plasma torch", "dark crystal", "reactive gel", "nano drone",
        "psi crystal", "neural dampener", "temporal crystal", "plasma net", "dark shard",
        "psi disruptor", "plasma blade", "plasma bomb", "dark vial", "quantum crystal",
        "psi lens", "warp stabilizer", "neural interface", "bio enhancer", "alien egg"
    }


    profiles = []

    for _ in range(n):
        species = random.choice(species_list)
        planet = random.choice(planet_list)
        has_visa = random.choice([True, False])
        criminal_record = random.choice([True, False])
        items = random.sample(item_pool, k=random.randint(1, 4))

        profile = {
            "species": species,
            "planet": planet,
            "has_visa": has_visa,
            "criminal_record": criminal_record,
            "items": items
        }

        profiles.append(profile)

    return profiles


aliens = generate_alien_profiles(5)
for i, alien in enumerate(aliens, 1):
    print(f"Alien {i}: {alien}")
