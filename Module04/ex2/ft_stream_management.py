import sys


class Logger:
    @staticmethod
    def info(msg: str) -> None:
        sys.stdout.write(f"[STANDARD] {msg}\n")

    @staticmethod
    def alert(msg: str) -> None:
        sys.stderr.write(f"[ALERT] {msg}\n")

    @staticmethod
    def input(msg: str) -> str:
        print(f"Input Stream active. {msg}", end='', flush=True)
        line = sys.stdin.readline()
        return line[:len(line)-1]


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    user_id = Logger.input("Enter archivist ID: ")
    user_status = Logger.input("Enter status report: ")

    print()

    Logger.info(f"Archive status from {user_id}: {user_status}")
    Logger.alert("System diagnostic: Sommunication channels verified")
    Logger.info("Data transmission complete")

    print("\nThree-channel communication test successful.")
