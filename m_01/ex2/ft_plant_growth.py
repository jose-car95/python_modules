#!/usr/bin/env python3


class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 1.0
    ) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age
        self.growth_rate: float = growth_rate

    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose: Plant = Plant("Rose", 25.0, 30, growth_rate=0.8)
    initial_height: float = rose.get_height()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(rose.get_info())
        rose.grow()
        rose.age()

    growth: float = rose.get_height() - initial_height
    print(f"Growth this week: {round(growth)}cm")


if __name__ == "__main__":
    main()
