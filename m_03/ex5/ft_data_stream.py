#!/usr/bin/env python3


import random
import time
from typing import Any, Generator


def game_events_stream(
        count: int, seed: int = 42
) -> Generator[dict[str, Any], None, None]:
    players: tuple = ("alice", "bob", "charlie", "pepe", "abel", "mario")
    event_types: tuple = ("kill", "treasure", "level_up")
    event_weights: tuple = (0.75, 0.10, 0.15)

    rng = random.Random(seed)

    for event_id in range(1, count + 1):
        player: str = rng.choice(players)
        level: int = rng.randint(1, 20)
        event_type: str = rng.choices(
            event_types, weights=event_weights, k=1
        )[0]
        yield {
            "id": event_id,
            "player": player,
            "level": level,
            "event_type": event_type
        }


def format_event(event: dict[str, Any]) -> str:
    player: str = event["player"]
    level: int = event["level"]
    event_type: str = event["event_type"]

    if event_type == "kill":
        action = "killed monster"
    elif event_type == "treasure":
        action = "found treasure"
    else:
        action = "leveled up"

    return f"Event {event['id']}: Player {player} (level {level}) {action}"


def process_stream(
        stream: Generator[dict[str, Any], None, None]
) -> tuple[int, int, int, int]:
    total: int = 0
    high_level: int = 0
    treasure: int = 0
    level_up: int = 0

    for event in stream:
        total += 1

        if event["level"] >= 10:
            high_level += 1
        if event["event_type"] == "treasure":
            treasure += 1
        elif event["event_type"] == "level_up":
            level_up += 1

    return total, high_level, treasure, level_up


def fibonacci_stream() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    i: int = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_stream() -> Generator[int, None, None]:
    n: int = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def print_from_generator(
        gen: Generator[int, None, None],
        n: int,
        label: str
) -> None:
    values: list[str] = []
    for _ in range(n):
        values.append(str(next(gen)))
    print(f"{label}: {', '.join(values)}")


def main() -> None:
    random.seed(42)
    print("=== Game Data Stream Processor ===")
    print()
    count: int = 1000
    print(f"Processing {count} game events...")
    print()
    preview_stream: Generator[dict[str, Any], None, None]
    preview_stream = game_events_stream(count)
    preview_n: int = 3
    i: int = 0
    while i < preview_n:
        ev: dict = next(preview_stream)
        print(format_event(ev))
        i += 1
    print("...")
    print()
    print("=== Stream Analytics ===")
    start: float = time.time()
    total, high_level, treasure, level_up = process_stream(
        game_events_stream(count)
    )
    end: float = time.time()
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f} seconds")
    print()
    print("=== Generator Demonstration ===")
    fib: Generator[int, None, None] = fibonacci_stream()
    print_from_generator(fib, 10, "Fibonacci sequence (first 10)")
    primes: Generator[int, None, None] = prime_stream()
    print_from_generator(primes, 5, "Prime numbers (first 5)")


if __name__ == "__main__":
    main()
