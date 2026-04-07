from abc import ABC, abstractmethod
from ex0.CreatureCard import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import Protocol, cast
from ex2.exceptions import InvalidStrategyCreatureError


class BattleStrategy(ABC):
    """Abstract strategy interface used by the tournament system."""
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Validate."""
        ...

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Action in combat."""
        ...


class TransformBattler(Protocol):
    """Structural type for objects that can attack, transform, and revert."""
    def attack(self) -> str:
        ...

    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class HealBattler(Protocol):
    """Structural type for objects that can attack and heal."""
    def attack(self) -> str:
        ...

    def heal(self) -> str:
        ...


# ===================================
# Diferents Strategies
# ===============================================
class NormalStrategy(BattleStrategy):
    """Default strategy: perform only a direct attack."""
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        """transform -> attack -> revert"""
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Transform-focused strategy: transform, attack, then revert."""
    def is_valid(self, creature: Creature) -> bool:
        """true si la criatura tiene transform/revert"""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        """transform -> attack -> revert"""
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        transformer: TransformBattler = cast(TransformBattler, creature)
        return (
            f"{transformer.transform()}\n"
            f"{transformer.attack()}\n"
            f"{transformer.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    """Heal-focused strategy: attack first, then heal."""
    def is_valid(self, creature: Creature) -> bool:
        """true si la criatura tiene heal"""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        """attack -> heal"""
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        healer: HealBattler = cast(HealBattler, creature)
        return f"{healer.attack()}\n{healer.heal()}"
