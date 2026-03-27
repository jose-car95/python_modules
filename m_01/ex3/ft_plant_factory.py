#!/usr/bin/env python3


class Plant:
    plants_created: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        Plant.plants_created += 1
        print(self.get_info())

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return (
            f"Created: {self._name}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)

    print("\nTotal plants created:", Plant.plants_created)
