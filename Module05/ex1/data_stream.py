from ..ex0.data_processor import (DataProcessor,
                                  NumericProcessor,
                                  TextProcessor,
                                  Log,
                                  LogProcessor)
from typing import Any


class DataStream:

    def __init__(self):
        self.processors: list[DataProcessor] = list()

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise Exception(f"Could not register {proc}: Not a DataProcessor!")
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            ingested = False
            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    ingested = True
                    break
            if not ingested:
                print("DataStream error - can't process the following element:"
                      f" {data}")

    def print_processors_stats(self) -> None:
        print("=== DataStrea statistics ===")
        if not self.processors:
            print("No processors found, no data to show")
        else:
            for processor in self.processors:
                print(f"{processor.__class__.__name__}: total "
                      f"{len(processor._storage) + processor._out_index} items"
                      " processed, "
                      f"remaining {len(processor._storage)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor...")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    data_stream = [10, 20, "hello",
                   Log("Hello World!", Log.Level.INFO),
                   Log("Critical Error!", Log.Level.ERROR),
                   ["this", "is", "a", "test"],
                   [5, 6]]

    print(f"\nSend first batch of data on stream: {data_stream}")
    ds.process_stream(data_stream)
    ds.print_processors_stats()

    print("\nRegistering other data processors...")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)
    print("Sending same data batch again...")
    ds.process_stream(data_stream)
    ds.print_processors_stats()

    print("\nConsume some elements for the processors...")
    for _ in range(2):
        num_proc.output()
    for _ in range(3):
        text_proc.output()
    log_proc.output()
    ds.print_processors_stats()
