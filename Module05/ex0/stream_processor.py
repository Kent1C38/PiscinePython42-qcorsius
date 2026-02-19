from typing import Any
from abc import abstractmethod
from abc import ABC


class Log:
    """A Log entry with a level of importance:
        0: Info
        1: Warn
        2: Error"""

    def __init__(self, content: str, level: int):
        self.__content = content
        self.__level = level

    def __str__(self):
        return f"{self.get_prefix()} {self.__content}"

    def get_prefix(self) -> str:
        match self.__level:
            case 0: return "[INFO]"
            case 1: return "[WARN]"
            case 2: return "[ALERT]"
            case _: return "[UNKNOWN]"

    def get_content(self) -> str:
        return self.__content


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process some data"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate your data's type, if it matches your processor"""
        pass

    def format_output(self, result: str) -> str:
        """Formats the result"""
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
    """Shows the right init sentence for your processor"""
    if isinstance(processor, TextProcessor):
        ttype = "Text"
    elif isinstance(processor, NumericProcessor):
        ttype = "Numeric"
    elif isinstance(processor, LogProcessor):
        ttype = "Log"
    else:
        ttype = "Unknown"

    print(f"Initializing {ttype} Processor...")


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
