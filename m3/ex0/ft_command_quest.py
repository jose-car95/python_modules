#!/usr/bin/env python3
import sys


def main(args: list[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    argc: int = len(args)
    if argc == 1:
        print("No arguments provided!")
    if argc > 1:
        print(f"Arguments received: {argc - 1}")
        i: int = 1
        while i < argc:
            print(f"Argument {i}: {args[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main(sys.argv)
