def check_temperature(temp_str: str) -> int:
    try:
        number = int(temp_str)
        if number < 0:
            print(f"Error: {number}°C is too cold for plants (min 0°C)")
        elif number > 40:
            print(f"Error: {number}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {number}°C is perfect for plants !")
            return number
        return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash !")


if __name__ == "__main__":
    test_temperature_input()
