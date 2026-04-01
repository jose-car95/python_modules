#!/usr/bin/env python3

import math


def distance_3d(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    )


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = user_input.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            invalid_value: str = str(e).split("'")[1]
            print(f"Error on parameter '{invalid_value}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    dist_center: float = distance_3d(pos1, origin)
    print(f"Distance to center: {round(dist_center, 4)}\n")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist_between: float = distance_3d(pos1, pos2)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
