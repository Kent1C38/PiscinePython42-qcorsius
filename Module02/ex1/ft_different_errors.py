def garden_operations(err_type: str):
    match err_type:
        case "value":
            int("abc")
        case "zero_division":
            1 / 0
        case "file_not_found":
            open("INVALID.txt")
        case "key":
            dico = {"test": "value"}
            dico["KO"]
        case _:
            return


def test_error_types():
    print("=== Garden Error Types Demo ===")

    operations = ["value", "zero_division", "file_not_found", "key"]

    for op in operations:
        try:
            print(f"\nTesting {op} error...")
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except KeyError as e:
            print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        for op in operations:
            garden_operations(op)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
