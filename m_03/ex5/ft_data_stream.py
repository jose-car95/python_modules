#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
    ]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        idx: int = random.randrange(len(events))
        yield events.pop(idx)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(gen)
        print(
            f"Event {i}: Player {event[0]} "
            f"did action {event[1]}"
        )
    events: list[tuple[str, str]] = [
        next(gen) for _ in range(10)
    ]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
