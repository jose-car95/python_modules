#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age

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


def main():
    rose = Plant("Rose", 25, 30)
    initial_height: int = rose.get_height()

    print("=== Day 1 ===")
    print(rose.get_info())

    rose.grow()
    rose.age()
    rose.grow()
    rose.age()
    rose.grow()
    rose.age()
    rose.grow()
    rose.age()
    rose.grow()
    rose.age()
    rose.grow()
    rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())

    growth: int = rose.get_height() - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
