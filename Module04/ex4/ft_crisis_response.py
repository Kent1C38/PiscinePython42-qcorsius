class FileAccess:
    def __init__(self, path: str):

        self.__path = path

        try:
            with open(path, "r") as file:
                self.__is_crisis = False
                self.__response = f"Archive recovered:\n'{file.read()}'"
                self.__status = "OK"
                self.__data = file.read()
                return
        except FileNotFoundError:
            self.__response = "Archive not found in storage matrix"
        except PermissionError:
            self.__response = "Security protocol: Access denied."

        self.__is_crisis = True
        self.__status = "System recovered, OK"

    def get_data(self) -> str:
        return self.__data

    def report(self) -> None:
        print(f"{'CRISIS ALERT' if self.__is_crisis else 'ROUTINE ACCESS'}:"
              + f" Attempting access to {self.__path}..."
              + f"\nRESPONSE: {self.__response}"
              + f"\nSTATUS: {self.__status}")


def test_file(file_path: str) -> None:
    access = FileAccess(file_path)
    access.report()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    test_file("lost_archive.txt")
    print()
    test_file("classified_data.txt")
    print()
    test_file("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully.")
