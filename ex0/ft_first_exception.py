def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if (temp >= 0 and temp <= 40):
        print(f"Temperature {temp}°C is perfect for plants!")
    elif (temp > 40):
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    try:
        tests = ["15", "abc", "100", "-50"]

        for temp in tests:
            print(f"\nTesting temperature: {temp}")
            check_temperature(temp)
        print("\nAll tests completed - program didn't crash!")
    except TypeError:
        print("Error: TypeError Raised !!!")


if __name__ == "__main__":
    test_temperature_input()
