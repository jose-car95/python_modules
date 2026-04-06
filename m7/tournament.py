#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory
from ex0.CreatureCard import CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy
)
from ex2.exceptions import InvalidStrategyCreatureError


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """
    Run a round-robin tournament where each pair fights once.
    Each opponent is defined by a factory and the strategy used by the
    base creature created from that factory.
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1: Creature = factory1.create_base()
            creature2: Creature = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategyCreatureError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    normal: NormalStrategy = NormalStrategy()
    aggressive: AggressiveStrategy = AggressiveStrategy()
    defensive: DefensiveStrategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive)
    ])
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive)
    ])
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive)
    ])


if __name__ == "__main__":
    main()
