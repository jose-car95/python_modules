#!/usr/bin/env python3

import sys


def parse_input(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty = arg.split(":", 1)
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def retrieve_max(inventory: dict) -> str:
    max: int = 0
    key: str = ""
    for k, v in inventory.items():
        if v > max:
            max = v
            key = k
    return key


def retrieve_min(inventory: dict[str, int]) -> str:
    min: int = (1 << 63) - 1
    key: str = ""
    for k, v in inventory.items():
        if v < min:
            min = v
            key = k
    return key


def main(args: list[str]) -> None:
    print("=== Inventory System Analysis ===")

    if len(args) == 1:
        print(
            "No inventory provided. Usage: "
            "python3 ft_inventory_system.py item:qty ..."
        )
        return
    inventory: dict[str, int] = parse_input(args)
    print(f"Got inventory: {inventory}")
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for name, qty in inventory.items():
        percent: float = (qty / total) * 100
        print(f"Item {name} represents {round(percent, 1)}%")
    if inventory:
        most_item: str = retrieve_max(inventory)
        least_item: str = retrieve_min(inventory)
        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main(sys.argv)
