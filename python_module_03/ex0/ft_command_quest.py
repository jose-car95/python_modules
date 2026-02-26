#!/usr/bin/env python3


import sys

list_arg: list[str] = sys.argv


def get_argv(list_arg) -> None:
    if len(list_arg) == 1:
        print("No arguments provided!")
    print(f"Program name: {list_arg[0]}")
    if len(list_arg) > 1:
        print(f"Arguments received: {len(list_arg) - 1}")
        i = 1
        while i < len(list_arg):
            print(f"Argument {i}: {list_arg[i]}")
            i += 1
    print(f"Total arguments: {len(list_arg)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    get_argv(sys.argv)
