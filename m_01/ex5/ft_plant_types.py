#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def grow(self, amount: float = 2.1) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> str:
        self._is_blooming = True
        return f"{self._name} is blooming beautifully!"

    def show(self) -> str:
        bloom_status: str = (
            f"{self._name} is blooming beautifully!"
            if self._is_blooming
            else f"{self._name} has not bloomed yet"
        )
        return f"{super().show()}\nColor: {self._color}\n{bloom_status}"


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> str:
        return (
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> str:
        return (
            f"{super().show()}\nTrunk diameter: {self._trunk_diameter:.1f}cm"
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = 0.0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self._nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 0.5

    def show(self) -> str:
        return (
            f"{super().show()}\n"
            f"Harvest season: {self._harvest_season}\n"
            f"Nutritional value: {round(self._nutritional_value)}"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    print("[asking the rose to bloom]")
    rose.bloom()
    print(rose.show())
    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    print(tomato.show())
