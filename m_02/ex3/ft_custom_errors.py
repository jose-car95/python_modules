#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_error(func, error_type: type[Exception], text: str) -> None:
    print(text)
    try:
        func()
    except error_type as e:
        print(f"Caught {error_type.__name__}: {e}")


def test_garden_error(func) -> None:
    try:
        func()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main():
    print("=== Custom Garden Errors Demo ===\n")

    test_error(check_plant, PlantError, "Testing PlantError...")
    print()
    test_error(check_water, WaterError, "Testing WaterError...")
    print()
    print("Testing catching all garden errors...")
    test_garden_error(check_plant)
    test_garden_error(check_water)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
