from abc import ABC, abstractmethod
from typing import Any
from enum import Enum


class Log:

    class Level(Enum):
        INFO = 1
        WARN = 2
        ERROR = 3

    def __init__(self, msg: str, level: Level):
        self.message = msg
        self.level = level

    def __str__(self) -> str:
        return f"[{self.level.name}] {self.message}"


class DataProcessor(ABC):

    def __init__(self):
        self._out_index: int = 0
        self._storage: list[str] = list()

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        try:
            out = (self._out_index, self._storage.pop(0))
        except IndexError:
            return None
        self._out_index += 1
        return out


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                return True
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if not self.validate(data):
            raise Exception("NumericProcessor cannot ingest this data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(x.__str__())
        else:
            self._storage.append(data.__str__())


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, str) for x in data):
                return True
        return False

    def ingest(self, data: str) -> None:
        if not self.validate(data):
            raise Exception("TextProcessor cannot ingest this data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(x)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, Log):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, Log) for x in data):
                return True
        return False

    def ingest(self, data: Log) -> None:
        if not self.validate(data):
            raise Exception("LogProcessor cannot ingest this data")

        if isinstance(data, list):
            for x in data:
                self._storage.append(x)
        else:
            self._storage.append(data)


if __name__ == "__main__":
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()

    print("=== Code Nexus - Data Processor ===")

    print("\n Testing with Numeric Processor...")
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'hello' {np.validate('hello')}")
    print("Trying to process invalid data without verification: ")
    try:
        np.ingest("foo")
    except Exception as e:
        print(f" Got: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values:")
    for _ in range(3):
        out = np.output()
        print(f"Numeric value {out[0]}: {out[1]}")

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value:")
    out = tp.output()
    print(f"Text value {out[0]}: {out[1]}")

    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {lp.validate('hello')}")
    print("Processing data: [Log('test', Log.Level.INFO), "
          "Log('hello', Log.Level.ERROR)]")
    lp.ingest([Log("test", Log.Level.INFO), Log("hello", Log.Level.ERROR)])
    print("Extracting 2 values:")
    for _ in range(2):
        out = lp.output()
        print(f"Log entry {out[0]}: {out[1]}")
