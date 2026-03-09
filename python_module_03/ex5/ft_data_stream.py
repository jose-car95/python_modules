#!/usr/bin/env python3


"""GENERADOR DE EVENTOS DEL JUEGO"""
def game_event_stream(n: int):
    """
    Debe devolver tuples tipo: (player, level, action)
    ("alice", 5, "killed monster")
    ("bob", 12, "found treasure")
    ("charlie", 8, "leveled up")
    """
    for i in range(n):
        # PLAYER
        if i % 3 == 0:
            player = "alice"
        elif i % 3 == 1:
            player = "bob"
        else:
            player = "charlie"

        # LEVEL
        level = (i % 15) + 1

        # ACTION
        if i % 3 == 0:
            action = "killed monster"
        elif i % 3 == 1:
            action = "found treasure"
        else:
            action = "leveled up"

        yield player, level, action

"""PROCESADOR QUE CONSUME EL STREAM"""


"""SISTEMA DE ESTADÍSTICAS SIN ALMACENAR TODO"""


"""COMPARACIÓN DE LISTAS VS GENERADORES"""
def big_list(n: int):
    """La lista guarda todos los datos"""
    result: list[int] = []
    for i in range(n):
        result.append(i)
    return result


def big_generator(n: int):
    """El generador produce 1 por 1"""
    for i in range(n):
        yield i


"""GENERADORES EXTRA -> (FIBONACCI Y PRIMOS)"""
def fibonacci():
    a: int = 0
    b: int = 1
    while True:
        yield a
        a,b = b, a + b


def primos():
    num: int = 2
    while True:
        yield num
        num += 1


"""FUNCIÓN PRINCIPAL -> GESTIONA TODA LA EJECUCIÓN DEL PROGRAMA"""
def main() -> None:
    total: int = 0
    high_level: int = 0
    treasure: int = 0
    level_up: int = 0

    for event in game_event_stream(1000):
        total += 1
        print(event)

    fib = fibonacci()
    for _ in range(10):
        print(next(fib))


if __name__ == "__main__":
    main()