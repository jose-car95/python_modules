#!/usr/bin/env python3


def water_plants(plant_list):
    print("Opening watering system")
    for plant in plant_list:
        if plant is None:
            raise ValueError
        else:
            print(f"Watering {plant}")
    print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===")

    plants = ["tomato", "lettuce", "carrots"]

    try:
        print("\nTesting normal watering...")
        water_plants(plants)
        print("\nTesting with error...")
        plants = ["tomato", None]
        water_plants(plants)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
