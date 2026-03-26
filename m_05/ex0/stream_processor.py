#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        """
        Default formatter that subclasses can override or reuse via super().
        """
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "NumericProcessor: invalid data, expected list of numbers"
            )
        numbers: list[int | float] = data
        count: int = len(numbers)
        total: float = float(sum(numbers)) if count else 0.0
        avg: float = (total / count) if count else 0.0

        total_display: str = (
            str(int(total)) if float(total).is_integer() else str(total)
        )
        avg_display: str = (
            f"{avg:.1f}"
        )

        result: str = (
           f"Processed {count} numeric values, "
           f"sum={total_display}, avg={avg_display}"
        )
        return result


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("TextProcessor: invalid data, expected a string")

        text: str = data
        length: int = len(text)
        words: int = len(text.split())
        result: str = (
            f"Processed text: {length} characters, {words} words"
        )
        return result


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "LogProcessor: invalid data, expected 'LEVEL: message' string"
            )

        entry: str = data
        level_raw: str
        message: str
        level_raw, _, message = entry.partition(":")
        level: str = level_raw.strip().upper()
        message_text: str = message.strip()

        if level == "ERROR":
            result: str = f"[ALERT] ERROR level detected: {message_text}"
        elif level == "WARNING":
            result = f"[NOTICE] WARNING level detected: {message_text}"
        else:
            result = f"[INFO] {level} level detected: {message_text}"
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric: DataProcessor = NumericProcessor()
    text: DataProcessor = TextProcessor()
    log: DataProcessor = LogProcessor()

    examples: list[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]

    processors_named: list[tuple[str, DataProcessor, Any]] = [
        ("Numeric Processor", numeric, examples[0]),
        ("Text Processor", text, examples[1]),
        ("Log Processor", log, examples[2]),
    ]

    for title, proc, data in processors_named:
        print(f"Initializing {title}...")
        if isinstance(data, str):
            print(f'Processing data: "{data}"')
        else:
            print(f"Processing data: {data}")

        try:
            valid: bool = proc.validate(data)
            if not valid:
                raise ValueError("validation failed")

            if isinstance(proc, NumericProcessor):
                print("Validation: Numeric data verified")
            elif isinstance(proc, TextProcessor):
                print("Validation: Text data verified")
            elif isinstance(proc, LogProcessor):
                print("Validation: Log entry verified")

            result_raw: str = proc.process(data)
            formatted: str = proc.format_output(result_raw)
            print(f"Output: {formatted}\n")
        except Exception as e:
            print(f"Validation: failed ({e})\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    demo_processors: list[DataProcessor] = [
        NumericProcessor(), TextProcessor(), LogProcessor()
    ]
    demo_data: list[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for idx, (proc, d) in enumerate(zip(demo_processors, demo_data), start=1):
        try:
            if not proc.validate(d):
                raise ValueError("validate failed")
            res: str = proc.process(d)
            out: str = proc.format_output(res)
            print(f"Result {idx}: {out}")
        except Exception as e:
            print(f"Result {idx}: failed ({e})")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
