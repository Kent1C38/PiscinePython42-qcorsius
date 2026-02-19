from typing import Any, Protocol, Union
from abc import ABC, abstractmethod
from json import loads
from io import StringIO
from csv import DictReader
from time import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> dict:
        print(f"Input: {data}")
        return data


class TransformStage():
    def process(self, data: Any) -> dict:
        print(f"Transform: {data}")
        return data


class OutputStage():
    def process(self, data: Any) -> str:
        print(f"Output: {data}")
        return data.__str__()


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str):
        self._stages: list[ProcessingStage] = list()
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self._stages.append(stage)

    def run_pipeline(self, data: Any) -> Any:
        current_data = data
        try:
            for stage in self._stages:
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

        try:
            parsed = loads(data)
        except Exception:
            print(f"Error parsing json to dict! ({self.pipeline_id})")
            return None

        return self.run_pipeline(parsed)


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            raw = StringIO(data.strip())
            reader = DictReader(raw)
            parsed = [x for x in reader]
        except Exception:
            print(f"Error parsing csv to dict! ({self.pipeline_id})")
            return None

        return self.run_pipeline(parsed)


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
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
        except Exception:
            print(f"Error parsing stream to dict! ({self.pipeline_id})")
            return None

        return parsed


if __name__ == "__main__":
    p = JSONAdapter("JSON-001")
    p.add_stage(InputStage())
    p.add_stage(TransformStage())
    p.add_stage(OutputStage())

    c = CSVAdapter("CSV-001")
    c.add_stage(InputStage())
    c.add_stage(OutputStage())

    p.process('{"test": 42, "name": "Nexus demo"}')
    print()
    c.process("""user,action,timestamp
Alice,login,2024-05-20
Bob,upload,2024-05-24""")
