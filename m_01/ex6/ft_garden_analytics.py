#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.__grow_calls: int = 0
            self.__age_calls: int = 0
            self.__show_calls: int = 0

        def add_grow(self) -> None:
            self.__grow_calls += 1

        def add_age(self) -> None:
            self.__age_calls += 1

        def add_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> str:
            return (
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, {self.__show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self.__stats: Plant._Stats = Plant._Stats()

    def grow(self, amount: float = 2.1) -> None:
        self._height += amount
        self.__stats.add_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self.__stats.add_age()

    def show(self) -> str:
        self.__stats.add_show()
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self) -> str:
        return self.__stats.display()

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> str:
        self._is_blooming = True
        return f"{self._name} is blooming beautifully!"

    def show(self) -> str:
        base: str = super().show()
        status: str = (
            f"{self._name} is blooming beautifully!"
            if self._is_blooming
            else f"{self._name} has not bloomed yet"
        )
        return f"{base}\nColor: {self._color}\n{status}"


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self.__shade_calls: int = 0

    def produce_shade(self) -> str:
        self.__shade_calls += 1
        return (
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> str:
        base: str = super().show()
        return f"{base}\nTrunk diameter: {self._trunk_diameter:.1f}cm"

    def display_stats(self) -> str:
        return f"{super().display_stats()}\n{self.__shade_calls} shade"


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count: int = 0

    def bloom(self, seeds: int = 0) -> str:
        self._seed_count = seeds
        return super().bloom()

    def show(self) -> str:
        return f"{super().show()}\nSeeds: {self._seed_count}"


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    print(plant.display_stats())


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    print(rose.show())
    display_plant_statistics(rose)
    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_plant_statistics(oak)
    print()

    print("=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(42)
    print(sunflower.show())
    display_plant_statistics(sunflower)
    print()

    print("=== Anonymous")
    unknown: Plant = Plant.create_anonymous()
    print(unknown.show())
    display_plant_statistics(unknown)


if __name__ == "__main__":
    main()
