from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_creture: str) -> None:
        self.name: str = name
        self.type_creature: str = self.type_creature

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> str:
        """
        return standard message using the name and the type of the Creature
        """
        pass


class CreatureFactory(Creature, ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class Flameling(CreatureFactory):
    def attack(self) -> str:
        """
        Appropriate string message
        """
        pass


class Pyrodon(Creature):
    def attack(self) -> str:
        """
        Appropriate string message
        """
        pass


class Aquabub(CreatureFactory):
    def attack(self) -> str:
        """
        Appropriate string message
        """
        pass


class Torragon(Creature):
    def attack(self) -> str:
        """
        Appropriate string message
        """
        pass


