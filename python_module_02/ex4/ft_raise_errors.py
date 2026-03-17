#!/usr/bin/env python3


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    if plant_name is not None and plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    def test(
            title: str, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        print(f"\n{title}")
        try:
            result: str | None = check_plant_health(
                plant_name, water_level, sunlight_hours
            )
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

    test("Testing good values...", "tomato", 5, 5)
    test("Testing empty plant name...", "", 5, 5)
    test("Testing bad water level...", "tomato", 15, 5)
    test("Testing bad sunlight hours...", "tomato", 5, 0)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
