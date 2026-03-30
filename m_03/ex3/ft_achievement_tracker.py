#!/usr/bin/env python3


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob: set = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set = {
        "level_10", "treasure_hunter",
        "boss_slayer", "speed_demon", "perfectionist"
    }
    print(f"Player alice achievement: {alice}")
    print(f"Player bob achievement: {bob}")
    print(f"Player bob achievement: {charlie}")
    print("\n=== Achievement Analytics ===")
    union = alice.union(bob, charlie)
    len_union: int = len(union)
    print(f"All unique achievements: {union}")
    print(f"Total unique achievement: {len_union}")
    common: set = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")
    rare_alice: set = alice.difference(bob.union(charlie))
    rare_bob: set = bob.difference(charlie.union(alice))
    rare_charlie: set = charlie.difference(alice.union(bob))
    rare: set = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achievement (1 player): {rare}\n")
    alice_vs_bob_common: set = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_vs_bob_common}")
    alice_unique: set = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique: set = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
