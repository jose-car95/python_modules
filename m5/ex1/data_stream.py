from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any], verbose: bool = True) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: str | None = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type
        }


# ---------------- SENSOR ----------------

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Sensor Stream...")
        super().__init__(stream_id, "Environmental Data")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any], verbose: bool = True) -> str:
        if verbose:
            print(f"Processing sensor batch: [{', '.join(data_batch)}]")

        temps: List[float] = []

        for item in data_batch:
            key, value = item.split(":")
            if key == "temp":
                temps.append(float(value))

        if not temps:
            raise ValueError("No temperature data")

        avg = sum(temps) / len(temps)

        result = (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg:.1f}°C"
        )

        if verbose:
            print(result)
        return result

    def filter_data(
        self, data_batch: List[Any], criteria: str | None = None
    ) -> List[Any]:
        if criteria == "high_priority":
            return [item for item in data_batch 
                    if item.startswith("temp:") and float(item.split(":")[1]) >= 30]
        return data_batch


# ---------------- TRANSACTION ----------------

class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Transaction Stream...")
        super().__init__(stream_id, "Financial Data")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any], verbose: bool = True) -> str:
        if verbose:
            print(f"Processing transaction batch: [{', '.join(data_batch)}]")

        total = 0

        for item in data_batch:
            kind, value = item.split(":")
            amount = int(value)

            if kind == "buy":
                total += amount
            elif kind == "sell":
                total -= amount

        result = (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {total:+d} units"
        )

        if verbose:
            print(result)
        return result

    def filter_data(
        self, data_batch: List[Any], criteria: str | None = None
    ) -> List[Any]:
        if criteria == "high_priority":
            return [item for item in data_batch 
                    if abs(int(item.split(":")[1])) >= 300]
        return data_batch


# ---------------- EVENT ----------------

class EventStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Event Stream...")
        super().__init__(stream_id, "System Events")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any], verbose: bool = True) -> str:
        if verbose:
            print(f"Processing event batch: [{', '.join(data_batch)}]")

        errors = sum(1 for item in data_batch if item.lower() == "error")

        result = (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} error detected"
        )

        if verbose:
            print(result)
        return result


# ---------------- PROCESSOR ----------------

class StreamProcessor:
    def process_all(
        self, streams: List[DataStream], batches: List[List[Any]]
    ) -> None:

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        print("Batch 1 Results:")

        # Mapeo de tipos para el output
        type_names = ["Sensor data", "Transaction data", "Event data"]
        item_names = ["readings processed", "operations processed", "events processed"]

        for i, (stream, batch) in enumerate(zip(streams, batches)):
            stream.process_batch(batch, verbose=False)  # Sin prints detallados
            print(f"- {type_names[i]}: {len(batch)} {item_names[i]}")

        print("\nStream filtering active: High-priority data only")

        # Usar filter_data() para mantener polimorfismo
        sensor_filtered = streams[0].filter_data(batches[0], "high_priority")
        trans_filtered = streams[1].filter_data(batches[1], "high_priority")

        print(
            f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
            f"{len(trans_filtered)} large transaction"
        )


# ---------------- MAIN ----------------

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor.process_batch(sensor_batch)

    print()
    transaction = TransactionStream("TRANS_001")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    transaction.process_batch(trans_batch)

    print()
    event = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    event.process_batch(event_batch)

    processor = StreamProcessor()

    batches = [
        ["temp:35.0", "temp:31.0"],
        ["buy:100", "sell:150", "buy:75", "buy:500"],
        ["login", "error", "logout"],
    ]

    processor.process_all([sensor, transaction, event], batches)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()