from collections.abc import Callable
from typing import Any


Counter = Callable[[], int]
Accumulator = Callable[[int], int]
Enchantment = Callable[[str], str]


def mage_counter() -> Counter:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Accumulator:
    total: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Enchantment:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any | str:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter_a: Counter = mage_counter()
    counter_b: Counter = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc: Accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming: Enchantment = enchantment_factory("Flaming")
    frozen: Enchantment = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
