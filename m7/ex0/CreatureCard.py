from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures in the game.
    Stores shared creature data (name and elemental type) and defines
    the required attack behavior for concrete creature cards.
    """
    def __init__(self, name: str, type_creature: str) -> None:
        """Initialize common creature identity fields."""
        self.name: str = name
        self.type_creature: str = type_creature

    @abstractmethod
    def attack(self) -> str:
        """Return the creature's attack action message."""
        ...

    def describe(self) -> str:
        """Return a generic description of this creature."""
        return f"{self.name} is a {self.type_creature} type Creature"


class CreatureFactory(ABC):
    """Abstract factory for creating a base/evolved pair from one family."""
    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base creature of a family."""
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved creature of a family."""
        ...


class FlameFactory(CreatureFactory):
    """Concrete factory for Fire-family creatures."""
    def create_base(self) -> Creature:
        """Create Flameling (base Fire creature)."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Create Pyrodon (evolved Fire creature)."""
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Concrete factory for Water-family creatures."""
    def create_base(self) -> Creature:
        """Create Aquabub (base Water creature)."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create Torragon (evolved Water creature)."""
        return Torragon()


class Flameling(Creature):
    """Base Fire creature card."""
    def __init__(self) -> None:
        """Initialize Flameling with fixed card metadata."""
        super().__init__(name="Flameling", type_creature="Fire")

    def attack(self) -> str:
        """Return Flameling's attack message."""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Evolved Fire creature card."""
    def __init__(self) -> None:
        """Initialize Pyrodon with fixed card metadata."""
        super().__init__(name="Pyrodon", type_creature="Fire/Flying")

    def attack(self) -> str:
        """Return Pyrodon's attack message."""
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Base Water creature card."""
    def __init__(self) -> None:
        """Initialize Aquabub with fixed card metadata."""
        super().__init__(name="Aquabub", type_creature="Water")

    def attack(self) -> str:
        """Return Aquabub's attack message."""
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Evolved Water creature card."""
    def __init__(self) -> None:
        """Initialize Torragon with fixed card metadata"""
        super().__init__(name="Torragon", type_creature="Water")

    def attack(self) -> str:
        """Return Torragon's attack message."""
        return f"{self.name} uses Hydro Pump!"
