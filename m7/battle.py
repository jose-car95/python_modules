#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory
from ex0.CreatureCard import CreatureFactory, Creature


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")

    creature1: Creature = factory1.create_base()
    creature2: Creature = factory2.create_base()

    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())

def main() -> None:
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
