#!/usr/bin/env python3


class Plant:
    plants_created: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Created: {self.get_info()}")
        Plant.plants_created += 1

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def grow(self) -> None:
        self.__height += 1

    def age(self) -> None:
        self.__age += 1

    def get_info(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    cactus: Plant = Plant("Cactus", 5, 90)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    fern: Plant = Plant("Fern", 15, 120)

    print("\nTotal plants created:", Plant.plants_created)
