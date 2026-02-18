#!/usr/bin/env python3


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    try:
        print("Testing normal watering...")
        water_plants(["tomato", "letuce", "carrots"])
        print("Watering completed successfully!")

        print("\nTesting with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
