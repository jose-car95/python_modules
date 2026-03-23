#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm "
                  f"[REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height: int = height
            print(f"Height update: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days "
                  f"[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age: int = age
            print(f"Age update: {self.__age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> str:
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: SecurePlant = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print("\nCurrent plant:", rose.get_info())
