#!/usr/bin/env python3


def garden_operations(error_type: str) -> None:
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        open("missing.txt")
    elif error_type == "key":
        data: dict[str, str] = {"plant": "Rose"}
        data["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
