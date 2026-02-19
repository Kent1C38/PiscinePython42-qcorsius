from typing import Optional, Any, Union
from abc import abstractmethod, ABC


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.count = 0

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        """Processes a batch of data"""
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        """Retrieve a list of filtered data"""
        if criteria is None:
            return data_batch

        return [item for item in data_batch if
                criteria.lower() in str(item).lower()]

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        """Retrieve stored stats"""
        return {"uid": self.stream_id, "processed": self.count}


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        self.count = len(data_batch)
        numbers = [x for x in data_batch if isinstance(x, (int, float))]
        self.avg = round(sum(numbers) / len(numbers), 2) if numbers else 0.0
        return (f"Sensor analysis: {self.stream_id} " +
                f"processed {self.count} items (avg: {self.avg})")

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria == "high_priority":
            return [x for x in data_batch if
                    isinstance(x, (int, float)) and x >= 30]
        else:
            return super().filter_data(data_batch, criteria)

    def get_stats(self) -> str:
        return super().get_stats() | {"average": self.avg}


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        self.count = len(data_batch)
        self.gains = sum(data_batch)
        return (f"Transaction analysis: {self.stream_id} " +
                f"processed {self.count} items (total gains: {self.gains})")

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria == "high_priority":
            return [x for x in data_batch if
                    isinstance(x, (int, float)) and
                    x < -200 or x > 200]
        else:
            return super().filter_data(data_batch, criteria)

    def get_stats(self) -> str:
        return super().get_stats() | {"gains": self.gains}


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        self.count = len(data_batch)
        self.errors = len([x for x in data_batch if isinstance(x, str)
                           and "error" in x.lower()])
        return (f"Event analysis:  {self.stream_id} " +
                f"processed {self.count} items (errors: {self.errors})")

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria == "high_priority":
            return [x for x in data_batch if isinstance(x, str)
                    and "error" in x.lower()]
        else:
            return super().filter_data(data_batch, criteria)


class StreamProcessor:

    def __init__(self):
        self.streams = {}

    def add_stream(self, stream: DataStream, data: list[Any]):
        """Add a stream in the process list"""
        self.streams[stream] = data

    def run(self, criteria=None):
        """Execute all streams in the process list"""
        print("\nRunning processor:")
        for stream, data in self.streams.items():
            try:
                if not isinstance(data, list):
                    raise ValueError(
                        f"Data for {stream.stream_id} must be a list")
                filtered = stream.filter_data(data, criteria)
                print(f"- {stream.process_batch(filtered)}")
            except Exception as e:
                print(f"Critical failure in {stream.stream_id}: {e}")


def stream_demo(stream: DataStream, data: list[Any]):
    """Demonstrate a stream process in detail"""
    if isinstance(stream, SensorStream):
        ttype = "Sensor"
    elif isinstance(stream, TransactionStream):
        ttype = "Transaction"
    elif isinstance(stream, EventStream):
        ttype = "Event"
    else:
        ttype = "Unknown"
    print(f"Initializing demo {ttype} Stream...")
    print(f"Stream ID: {stream.stream_id}")
    print(f"Processing batch: {data}")
    result = stream.process_batch(data)
    print(f"Data analysis: {result}")
    print(f"Stored statistics: {stream.get_stats()}")

    print("\nTrying with filter 'high_priority'...")
    filterd = stream.filter_data(data, "high_priority")
    result = stream.process_batch(filterd)
    print(f"Data analysis: {result}")
    print(f"Stored statistics: {stream.get_stats()}")
    print()


def polymorphism_demo(criteria=None):
    """Demonstrate the usage of the DataStream interface"""
    proc = StreamProcessor()

    proc.add_stream(SensorStream("SENSOR-001"), [20, "test", 35])
    proc.add_stream(TransactionStream("TRANS-001"), [-300, 50, 430, -10])
    proc.add_stream(EventStream("EVENT-001"),
                    ["login", "Error: denied", "logout"])

    proc.run(criteria)


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    stream_demo(SensorStream("SENSOR-DEMO"), [10, 20, 35, 5, -2, 3, 8])

    stream_demo(TransactionStream("TRANS-DEMO"),
                [20, -30, 300, 51, -249, -800, 900])

    stream_demo(EventStream("EVENT-DEMO"),
                ["login", "login", "logout", "error", "auth", "error"])

    print("\nPolymorphism Demo")
    polymorphism_demo()

    print("\nPolymorphism Filtered Demo")
    polymorphism_demo("high_priority")
