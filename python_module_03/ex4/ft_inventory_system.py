#!/usr/bin/ven python3


def print_inventory_info(inventory: dict) -> None:
    for item in inventory.items():
        sub_dict: dict = item[1]
        print(f"{item[0]} ({sub_dict.get('category')}, "
              f"{sub_dict.get('rarity')}): "
              f"{sub_dict.get('quantity')}x @ "
              f"{sub_dict.get('value')} gold each = "
              f"{sub_dict.get('value') * sub_dict.get('quantity')}"
              )


def value_inventory(inventory: dict) -> None:
    total_items: int = 0
    total_value: int = 0
    categories: dict = {}
    for item in inventory.items():
        sub_dict: dict = item[1]

        total_items += sub_dict.get('quantity')
        total_value += sub_dict.get('value') * sub_dict.get('quantity')

        cat: str = sub_dict.get('category')
        quantity: int = sub_dict.get('quantity')
        categories[cat] = quantity

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    category_string: list = []
    for item in categories.items():
        category_string.append(f"{item[0]}({item[1]})")
    categories_final: str = ", ".join(category_string)
    print(f"Categories: {categories_final}")


def transaction_potions(inv_from: dict, inv_to: dict, qty: int) -> None:
    if inv_from.get('potion') is None:
        print("Transaction unsuccessful!")
        return
    elif inv_from.get('potion').get('quantity') < qty:
        print("Transaction unsuccessful!")
        return
    inv_from['potion']['quantity'] -= qty
    try:
        inv_to['potion']['quantity'] += qty
    except KeyError:
        inv_to['potion'] = {
            'category': 'consumable',
            'rarity': 'common',
            'quantity': qty,
            'value': 50
        }
        print("Transaction successful!")


def most_value(inventories: dict) -> None:
    player_name: str = ""
    max_value: int = 0
    for name, inventory in inventories.items():
        total_value: int = 0
        for obj in inventory.values():
            total_value += obj.get('quantity') * obj.get('value')
        if total_value > max_value:
            max_value = total_value
            player_name = name
    print(f"Most valuable player: {player_name.capitalize()} "
          f"({max_value} gold)"
          )


def most_items(inventory: dict) -> None:
    player_name: str = ""
    max_items = 0
    for name, inventory in inventory.items():
        total_items: int = 0
        for obj in inventory.values():
            total_items += obj.get('quantity')
        if total_items > max_items:
            max_items = total_items
            player_name = name
    print(f"Most items: {player_name.capitalize()} ({max_items} items)")


def rarest_items(inventories: dict) -> None:
    rare_items: list = []
    for inventory in inventories.values():
        for item_name, attributes in inventory.items():
            if attributes.get('rarity') == "rare":
                rare_items.append(item_name)
    result: str = ", ".join(rare_items)
    print(f"Rarest items: {result}")


def main() -> None:
    alice_inventory: dict = {
        'sword': {
            'category': 'weapon',
            'rarity': 'rare',
            'quantity': 1,
            'value': 500
        },
        'potion': {
            'category': 'consumable',
            'rarity': 'common',
            'quantity': 5,
            'value': 50
        },
        'shield': {
            'category': 'armor',
            'rarity': 'uncommon',
            'quantity': 1,
            'value': 200
        }
    }
    bob_inventory: dict = {
        'axe': {
            'category': 'weapon',
            'rarity': 'common',
            'quantity': 1,
            'value': 80
        },
        'magic_ring': {
            'category': 'armor',
            'rarity': 'rare',
            'quantity': 1,
            'value': 200
        }
    }
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    print_inventory_info(alice_inventory)
    print()
    value_inventory(alice_inventory)
    print()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    transaction_potions(alice_inventory, bob_inventory, 2)
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion'].get('quantity')}")
    print(f"Bob potions: {bob_inventory['potion'].get('quantity')}")
    inventories: dict = {'alice': alice_inventory, 'bob': bob_inventory}
    print("\n=== Inventory Analytics ===")
    most_value(inventories)
    most_items(inventories)
    rarest_items(inventories)


if __name__ == "__main__":
    main()
