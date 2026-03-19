#!usr/bin/env python3


import sys


def parse_input(args: list[str]) -> dict:
    inventory: dict = {}
    for arg in args[1:]:
        name, qty = arg.split(":")
        inventory[name] = int(qty)
    return inventory


def print_analysis(inventory: dict) -> None:
    total_items: int = 0
    for value in inventory.values():
        total_items += value
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")


def print_inventory(inventory: dict) -> None:
    total: int = 0
    for value in inventory.values():
        total += value
    print("=== Current Inventory ===")

    for name, qty in sorted(
            inventory.items(), key=lambda item: item[1], reverse=True
    ):
        percent: float = (qty / total) * 100
        print(f"{name}: {qty} units ({percent:.1f}%)")
    print()


def print_stats(inventory: dict) -> None:
    max_item: str = ""
    min_item: str = ""
    max_qty: int = -1
    min_qty: int = 999999
    for name, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_item = name
        if qty < min_qty:
            min_qty = qty
            min_item = name
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {max_item} ({max_qty} units)")
    print(f"Least abundant: {min_item} ({min_qty} units)\n")


def categorize_items(inventory: dict) -> None:
    categories: dict = {
        "Moderate": {},
        "Scarce": {}
    }
    for name, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty
    print("=== Item Categories ===")
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}\n")


def suggest_restock(inventory: dict) -> None:
    low_item: list = []
    for name, qty in inventory.items():
        if qty <= 1:
            low_item.append(name)
    result: str = ", ".join(low_item)
    print("=== Management Suggestions ===")
    print(f"Restock needed: {result}\n")


def dictionary_demo(inventory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {", ".join(inventory.keys())}")
    value_list: list = []
    for v in inventory.values():
        value_list.append(str(v))
    print(f"Dictionary values: {", ".join(value_list)}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main(args: list[str]) -> None:
    if len(args) == 1:
        print("Error: No inventory data provided.")
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        return
    inventory: dict = parse_input(args)
    print_analysis(inventory)
    print_inventory(inventory)
    print_stats(inventory)
    categorize_items(inventory)
    suggest_restock(inventory)
    dictionary_demo(inventory)


if __name__ == "__main__":
    main(sys.argv)
