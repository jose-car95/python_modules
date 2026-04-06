from abc import ABC, abstractmethod
from ex0.CreatureCard import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):
    def is_valid(self) -> bool:
        """Esta criatura es complatible con esta estrategia?"""
        pass

    def act(self, creature) -> str:
        """Que hace en combate?"""
        pass


class NormalStrategy(BattleStrategy, Creature):
    """Compatible con cualquier criatura"""
    def is_valid() -> bool:
        return True

    def act(self, creature) -> str:
        """transform -> attack -> revert"""
        pass


class AggressiveStrategy(BattleStrategy, TransformCapability):
    """Compatible con TransformCapability"""
    def is_valid(self):
        """true si la criatura tiene transform/revert"""
        pass

    def act(self, creature) -> str:
        """transform -> attack -> revert"""
        pass


class DefensiveStrategy(BattleStrategy, HealCapability):
    """compatible con HealCapability"""
    def is_valid(self):
        """true si la criatura tiene heal"""
        pass

    def act(self, creature) -> str:
        """attack -> heal"""
        pass