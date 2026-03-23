#!/usr/bin/env python3


import sys


def get_argv(args: list[str]) -> None:
    print("=== Command Quest ===")
    argc: int = len(args)
    if argc == 1:
        print("No arguments provided!")
    print(f"Program name: {args[0]}")
    if argc > 1:
        print(f"Arguments received: {argc - 1}")
        i: int = 1
        while i < argc:
            print(f"Argument {i}: {args[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    get_argv(sys.argv)
