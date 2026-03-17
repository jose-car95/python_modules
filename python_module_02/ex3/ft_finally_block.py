#!/usr/bin/env python3


def close_system() -> None:
    print("Closing watering system (cleanup)")


def water_plants(plant_list: list[str | None]) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant is None:
            raise ValueError("Cannot water None - invalid plant!")
        else:
            print(f"Watering {plant}")
    close_system()
    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    plants: list[str] = ["tomato", "lettuce", "carrots"]
    plants_with_error: list[str | None] = ["tomato", None]

    try:
        print("\nTesting normal watering...")
        water_plants(plants)
        print("\nTesting with error...")
        water_plants(plants_with_error)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        close_system()

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
