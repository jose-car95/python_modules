from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


"""
reduce:
    Combina todos los elementos de una secuencia en un único valor
    aplicando una función acumulativa.
operator.add y operator.mul:
    Funciones ya preparadas para suma y multiplicación,
    y encajan muy bien con 'reduce'.

"""


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
    """Fijar algunos argumentos de una función para crear variantes más especializadas"""
    """
        partial:
            sirve para fijar algunos argumentos de una funcion por adelantado
    """
    pass


def memoized_fibonacci(n: int) -> int:
    """Enseña memoización con lru_cache"""
    """
        lru_cache:
            @lru_cache:
                introduce memoizacion
                Memoizar:
                    Guardar el resultado de una llamada para no recalcularlo si vuelves a pedir lo mismo.
    """
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    """Enseña despacho por tipo con singledispath"""
    """
        singledispath:
            te deja crear una funcion genérica cuyo comportamiento cambia
            según el tipo de argumento
    """
    pass


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


if __name__ == "__main__":
    main()
