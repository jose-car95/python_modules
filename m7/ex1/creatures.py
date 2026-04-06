from .capabilities import HealCapability, TransformCapability
from ex0.CreatureCard import Creature


class Sproutling(Creature, HealCapability):
    """Base Grass creature with healing capability."""
    def __init__(self) -> None:
        super().__init__(name="Sproutling", type_creature="Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved Grass/Fairy creature with stronger healing capability."""
    def __init__(self) -> None:
        super().__init__(name="Bloomelle", type_creature="Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base Normal creature that changes attack behavior while transformed."""
    def __init__(self) -> None:
        super().__init__(name="Shiftling", type_creature="Normal")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved Normal/Dragon creature with transform-base attack flow."""
    def __init__(self) -> None:
        super().__init__(name="Morphagon", type_creature="Normal/Dragon")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
