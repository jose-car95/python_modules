#!/usr/bin/env python3
from ex0.CreatureCard import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base: Creature = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    evolved: Creature = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    base: Creature = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    evolved: Creature = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


def main() -> None:
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()

    test_healing_factory(healing_factory)
    print()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
