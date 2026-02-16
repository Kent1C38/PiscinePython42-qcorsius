import sys


class Logger:
    @staticmethod
    def info(msg: str) -> None:
        sys.stdout.write(f"[STANDARD] {msg}\n")

    @staticmethod
    def severe(msg: str) -> None:
        sys.stderr.write(f"[ERROR] {msg}\n")

    @staticmethod
    def warn(msg: str) -> None:
        sys.stderr.write(f"[WARN] {msg}\n")


class SecureVault:
    def __init__(self, path: str):
        self.__path = path

    def extract(self) -> str:
        Logger.info("Secure Extraction starting...")
        try:
            with open(self.__path, "r") as archive:
                data = archive.read()
                Logger.info(f"Data extracted:\n{data}")
                return data
        except FileNotFoundError:
            Logger.severe(f"File not found: {self.__path}")
            return None

    def preserve(self, data: str):
        Logger.info("Secure Preservation starting...")
        try:
            with open(self.__path, "x") as archive:
                archive.write(data)
                Logger.info(f"Securing data:\n{data}")
        except FileExistsError:
            Logger.warn("Cannot overwrite existing data!")


if __name__ == "__main__":
    vault = SecureVault("secure_vault.txt")
    data = vault.extract()
    vault.preserve("""CLASSIFIED: Python is such a boring language""")
    print()
    vault.preserve("""CLASSIFIED: This is a test""")
    print()
    data = vault.extract()
