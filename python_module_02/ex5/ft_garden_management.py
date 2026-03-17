#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self) -> None:
        self.plants: list[str | None] = []

    def add_plant(self, plant: str) -> None:
        if not plant:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants = self.plants + [plant]
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            if plant is None:
                raise WaterError()
            print(f"Watering {plant} - success")
        print("Closing watering system (Cleanup)")

    def check_health(self, plant: str, water: int, sun: int) -> None:
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        print(f"{plant}: healthy (water: {water}, sun: {sun})")

    def check_tank(self) -> None:
        raise WaterError("Caught GardenError: Not enough water in tank")


def check_system() -> None:
    print("=== Garden Management System ===")
    manager: GardenManager = GardenManager()
    plant_list: list[str] = ["tomato", "letuce", ""]
    print("\nAdding plants to garden...")
    for plant in plant_list:
        try:
            manager.add_plant(plant)
        except PlantError as e:
            print(e)
    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(e)
    plant_list = ["tomato", "lettuce"]
    print("\nChecking plant health...")
    for plant in plant_list:
        try:
            manager.check_health(plant, 5 if plant == "tomato" else 15, 8)
        except PlantError as e:
            print(f"Error checking {plant}: {e}")
    print("\nTesting error recovery...")
    try:
        manager.check_tank()
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    check_system()
