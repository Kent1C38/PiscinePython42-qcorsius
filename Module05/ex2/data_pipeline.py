from typing import Protocol, Any
from ..ex0.data_processor import (DataProcessor,
                                  NumericProcessor,
                                  TextProcessor,
                                  LogProcessor,
                                  Log)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        export = ""
        for index, item in enumerate(data):
            export = (f"{export}{',' if index != 0 and item else ''}" +
                      f"{item[1] if item else ''}")
        print("CSV Output:")
        print(export)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        export = dict()
        for index, item in enumerate(data):
            if item:
                export[f"item_{index + 1}"] = item[1].__str__()
        print("JSON Output:")
        print(export)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        for processor in self.processors:
            batch = []
            for _ in range(nb):
                batch.append(processor.output())
            plugin.process_output(batch)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()

    print("\nRegistering Processors...")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    data_batch = ["Hello World!", [3.14, -1, 2.71],
                  [Log("Telnet access! Use ssh instead", Log.Level.WARN),
                   Log("User wil is connected", Log.Level.INFO)],
                  42, ["Hi", "five"]]
    print(f"\nSend first data batch on stream: {data_batch}")
    ds.process_stream(data_batch)

    print()
    print(ds.print_processors_stats())

    print("\nSend 3 processed data for each processor to CSV Plugin...")
    ds.output_pipeline(3, CSVPlugin())

    print()
    ds.print_processors_stats()

    data_batch2 = [21, ["fk generative AI", "Why LLMs ??", "Stay healthy"],
                   [Log("500 server crash", Log.Level.ERROR),
                    Log("Certificate expires in 10 days", Log.Level.INFO)],
                   [32, 42, 64, 84, 128, 168], "World Hello"]
    print(f"\nSend another batch of data: {data_batch2}")
    ds.process_stream(data_batch2)

    print()
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to JSON Plugin")
    ds.output_pipeline(5, JSONPlugin())

    print()
    ds.print_processors_stats()
