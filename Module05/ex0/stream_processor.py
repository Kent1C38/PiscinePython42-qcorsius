from typing import Any
from abc import abstractmethod
from abc import ABC


class Log:

    def __init__(self, content: str, level: int):
        self.__content = content
        self.__level = level
        match self.__level:
            case 0: self.__prefix = "[INFO]"
            case 1: self.__prefix = "[WARN]"
            case 2: self.__prefix = "[ALERT]"
            case _: self.__prefix = "[UNKNOWN]"

    def __str__(self):
        return f"{self.__prefix} {self.__content}"

    def get_prefix(self) -> str:
        return self.__prefix

    def get_content(self) -> str:
        return self.__content


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Processed data: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: list[int]) -> str:
        return f"sum={sum(data)}, avg={sum(data)/len(data)}"

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(isinstance(item, int) for item in data))

    def format_output(self, result: str) -> str:
        return f"Processed numerical data: {result}"


class TextProcessor(DataProcessor):

    def process(self, data: str) -> str:
        return f"{len(data)} characters, {len(data.split(' '))} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return f"Processed text data: {result}"


class LogProcessor(DataProcessor):

    def process(self, data: Log) -> str:
        return str(data)

    def validate(self, data: Any) -> bool:
        return isinstance(data, Log)

    def format_output(self, result: str) -> str:
        return f"Processed Log: {result}"


def init_processor(processor: DataProcessor) -> None:
    if isinstance(processor, TextProcessor):
        print("Initializing Text Processor...")
    elif isinstance(processor, NumericProcessor):
        print("Initializing Numeric Processor...")


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    stream_line = {NumericProcessor(): [1, 2, 3, 4, 5],
                   TextProcessor(): "This is a test data sample.",
                   LogProcessor(): Log("This works !", 0)}

    for processor, data in stream_line.items():
        print()
        init_processor(processor)
        print(f"Processing data: {data}")
        is_valid = processor.validate(data)
        if is_valid:
            print("Data type validation: OK")
            print(
                f"Output: {processor.format_output(processor.process(data))}")
        else:
            print("Data type validation: KO")
