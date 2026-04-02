#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")
    all_capitalized: list[str] = [
        name.capitalize() for name in players
    ]
    only_capitalized: list[str] = [
        name for name in players if name[0].isupper()
    ]
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}")
    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_capitalized
    }
    print(f"\nScore dict: {scores}")
    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")
    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
