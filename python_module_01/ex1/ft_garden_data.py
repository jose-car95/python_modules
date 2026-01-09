#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    print(rose.get_info())
    print(sunflower.get_info())
    print(cactus.get_info())


if __name__ == "__main__":
    main()
