from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Any] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning")
    }


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment with {power} power on {target}"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch_spell(value: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch_spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch_spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch_spell


def main() -> None:
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")
    print(f"Min: {spell_reducer([10, 20, 30, 40], 'min')}")
    print(f"Empty: {spell_reducer([], 'add')}")
    try:
        print(spell_reducer([1, 2, 3], 'unknown'))
    except ValueError as error:
        print(error)

    print("\nTesting partial enchanter")
    enchanted = partial_enchanter(enchant)
    print(enchanted["fire"]("Sword"))
    print(enchanted["ice"]("Shield"))
    print(enchanted["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    disparcher = spell_dispatcher()
    print(disparcher(42))
    print(disparcher("fireball"))
    print(disparcher(["fireball", "heal", "shield"]))
    print(disparcher(3.14))


if __name__ == "__main__":
    main()
