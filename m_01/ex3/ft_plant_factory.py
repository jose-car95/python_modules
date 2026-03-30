#!/usr/bin/env python3


class Plant:
    plants_created: int = 0

    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 1.0
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.growth_rate: float = growth_rate
        print(self.get_info())

    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> str:
        return (
            f"Created: {self.name}: "
            f"{self.height:.1f}cm, {self.age} days old"
        )

    def grow(self) -> None:
        self.height += self.growth_rate
        self.age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)
