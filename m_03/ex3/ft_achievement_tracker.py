#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    achievements_pool: list[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind",
        "Unstoppable", "Hidden Path Finder"
    ]
    num: int = random.randint(3, len(achievements_pool))
    return set(random.sample(achievements_pool, num))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_achievements}")

    common: set[str] = set.intersection(*players.values())
    print(f"\nCommon achievements: {common}\n")

    for name, achievements in players.items():
        others: set[str] = set().union(
            *(v for k, v in players.items() if k != name)
        )
        unique: set[str] = achievements.difference(others)
        print(f"Only {name} has: {unique}")
    print()

    for name, achievements in players.items():
        missing: set[str] = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
