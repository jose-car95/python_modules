#!/usr/bin/env python3


import sys
import math


def distance_3d(
        x1: int, y1: int, z1: int,
        x2: int, y2: int, z2: int
) -> float:
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))


def parse_coordinates(
        args: list[str], pos: int
) -> tuple[int, int, int] | None:
    position: tuple[int, int, int]
    try:
        position = (
            int(args[pos].split(',')[0]),
            int(args[pos].split(',')[1]),
            int(args[pos].split(',')[2])
        )
        return position
    except ValueError as e:
        print(f'\nParsing invalid coordinates: "{args[pos]}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")


def main(args: list[str]) -> None:
    print("=== Game Coordinate System ===")
    position: tuple = (10, 20, 5)
    player: tuple = (0, 0, 0)
    print(f"\nPosition created: {position}")
    print(
        f"Distance between {player} and "
        f"{position}: {distance_3d(*position, *player):.2f}"
    )

    argc: int = len(sys.argv)
    if argc == 3:
        print(f'\nParsing coordinates: "{args[1]}"')
        try:
            new_position: tuple = parse_coordinates(args, 1)
            print(f"Parse position: {new_position}")
            print(
                f"Distance between {player} and {new_position}: "
                f"{distance_3d(*new_position, *player):.1f}"
            )
        except TypeError:
            return
        try:
            parse_coordinates(args, 2)
        except TypeError:
            return
    else:
        print(
            "\nError ARGS: Please use the program this way:",
            'python3 ft_coordinate_system.py "X1,Y1,Z1" "X2,Y2,Z2"'
        )
    position = (3, 4, 0)
    print("\nUnpacking demonstration:")
    print("Player at: x=%d, y=%d, z=%d" % position)
    print("Coordinates: X=%d, Y=%d, Z=%d" % position)


if __name__ == "__main__":
    main(sys.argv)
