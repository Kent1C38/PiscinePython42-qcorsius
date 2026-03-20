from typing import Any, Protocol, Union
from abc import ABC, abstractmethod
from json import loads, dumps
from io import StringIO
from csv import DictReader
from time import time, perf_counter


class ConversionError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> dict:
        print(f"Input: {type(data)} {data}")
        return data


class TransformStage:
    def process(self, data: Any) -> dict:
        payload = data if isinstance(data, dict) else {"raw_data": data}

        transformed = {
            k: [
                {sub_k: (sub_v.upper() if isinstance(sub_v, str) else sub_v)
                 for sub_k, sub_v in item.items()} for
                item in v if isinstance(item, dict)]
            if isinstance(v, list)
            else (v.upper() if isinstance(v, str) else v)
            for k, v in payload.items()
        }
        print(f"Transform: {type(transformed)} {transformed}")
        return transformed


class OutputStage():
    def process(self, data: Any) -> str:
        out = data.__str__()
        print(f"Output: {type(out)} {data}")
        return out


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str):
        self.__stages: list[ProcessingStage] = list()
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.__stages.append(stage)

    def run_pipeline(self, data: Any) -> Any:
        current_data = data
        try:
            for stage in self.__stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            print(f"Catched error in pipeline: {e}")

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Attempting JSON conversion...")
        try:
            if isinstance(data, dict):
                return self.run_pipeline(data)
            if isinstance(data, list):
                parsed = dumps(data, indent=2)
            else:
                parsed = loads(data)

            return self.run_pipeline(parsed)
        except Exception as e:
            raise ConversionError(
                f"Error parsing json to dict!: {e} ({self.pipeline_id})")
            return None


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Attempting CSV conversion...")
        try:
            if isinstance(data, (dict, list)):
                return self.run_pipeline(data)
            raw = StringIO(data.strip())
            reader = DictReader(raw)
            parsed = {"rows": [x for x in reader]}
        except Exception as e:
            raise ConversionError(
                f"Error parsing csv to dict!: {e} ({self.pipeline_id})")
            return None

        return self.run_pipeline(parsed)


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Attempting stream (packet) conversion...")
        try:
            if isinstance(data, list):
                parsed = {
                    "stream_source": self.pipeline_id,
                    "reading_count": len(data),
                    "payload": data,
                    "timestamp": time()
                }
            else:
                parsed = {"data": data, "type": "single_event"}
        except Exception as e:
            raise ConversionError(
                f"Error parsing stream to dict! {e} ({self.pipeline_id})")

        return self.run_pipeline(parsed)


class NexusManager():

    def __init__(self):
        self.__pipelines: list[ProcessingPipeline] = list()

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.__pipelines.append(pipeline)

    def process_data(self, data: Any):
        print("Starting pipeline processing...")
        start = perf_counter()
        processed_data = 0

        current = data
        try:
            for processor in self.__pipelines:
                current = processor.process(current)
                processed_data += 1
                print()
        except ConversionError as e:
            print(f"Exception caught during pipeline run: {e}")
            return
        finally:
            self.__pipelines = list()
            print("Cleaned up pipeline")

        end = perf_counter()
        elapsed = end - start
        print("---- Result ----")
        print(current)
        print("\n---- Pipeline Statistics ----")
        print(f"Processed data {processed_data} times through this pipeline " +
              f"in {elapsed:.6f}s")


def test_csv_to_json_packet():
    nexus = NexusManager()

    j = JSONAdapter("JSON-001")
    j.add_stage(InputStage())

    s = StreamAdapter("Stream-001")
    s.add_stage(InputStage())
    s.add_stage(OutputStage())

    c = CSVAdapter("CSV-001")
    c.add_stage(InputStage())
    c.add_stage(TransformStage())

    nexus.add_pipeline(c)
    nexus.add_pipeline(j)
    nexus.add_pipeline(s)

    nexus.process_data("name,value\ntest,42\nkent,38")


def test_json_error():

    nexus = NexusManager()

    j = JSONAdapter("JSON-002")
    j.add_stage(InputStage())
    j.add_stage(TransformStage())
    j.add_stage(OutputStage())

    nexus.add_pipeline(j)

    nexus.process_data("{\"test\': 42}")  # invalid data


if __name__ == "__main__":
    print("=== CODE NEXUS DEMO ===")

    print("\n=== Trying with a complete pipeline" +
          ": CSV -> JSON -> Stream (packet) ===")
    test_csv_to_json_packet()

    print("\n=== Trying with an invalid data (json) ===")
    test_json_error()
