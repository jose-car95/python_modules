def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:
    artifacts: list[dict] = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Ring", "power": 78, "type": "jewelry"}
    ]
    mages: list[dict] = [
        {"name": "Aeris", "power": 80, "element": "fire"},
        {"name": "Borin", "power": 45, "element": "earth"},
        {"name": "Lyra", "power": 90, "element": "air"}
    ]
    spells: list[str] = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts: list[dict] = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")
    first: dict = sorted_artifacts[0]
    second: dict = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power)"
        f" comes before {second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter...")
    strong_mages: list[dict] = power_filter(mages, 70)
    for mage in strong_mages:
        print(f"{mage['name']} reaches {mage['power']} power")

    print("\nTesting spell transformer...")
    transformer_spells = spell_transformer(spells)
    print(*transformer_spells)

    print("\nTesting mage stats...")
    stats: dict = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
