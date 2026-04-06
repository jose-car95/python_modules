from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_creature: str) -> None:
        self.name: str = name
        self.type_creature: str = type_creature

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type_creature} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


# =============================================

class FlameFactory(CreatureFactory):
    """Crea objetos de la familia Fire -> Crea la criatura"""
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Crea objetos de la familia Water -> Crea la criatura"""
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


# ==========================================

class Flameling(Creature):
    """Fire family"""
    def __init__(self) -> None:
        super().__init__(name="Flameling", type_creature="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Fire family -> Evolución Flameling"""
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type_creature="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Water family"""
    def __init__(self) -> None:
        super().__init__(name="Aquabub", type_creature="Water")

    def attack(self) -> str:
       return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Water family -> Evolución Aquabub"""
    def __init__(self) -> None:
        super().__init__(name="Torragon", type_creature="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
