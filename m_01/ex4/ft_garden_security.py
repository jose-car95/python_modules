#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)

        print(
            f"Plant created: {self._name}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {self._height:.0f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: SecurePlant = SecurePlant("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-2)
    print()
    print("Current state:", rose.get_info())
