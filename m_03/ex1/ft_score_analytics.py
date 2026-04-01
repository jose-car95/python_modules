#!/usr/bin/env python3


import sys


def parse(args: list[str]) -> list[int]:
    list_number: list[int] = []
    for arg in args[1:]:
        try:
            list_number.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return list_number


def analytics_score(scores: list[int]) -> None:
    print(f"Score processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores) / len(scores)):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main(args: list[str]) -> None:
    print("=== Player Score Analytics ===")
    argc: int = len(args)
    scores: list[int] = parse(args)
    if argc < 2 or not scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
    else:
        analytics_score(scores)


if __name__ == "__main__":
    main(sys.argv)
