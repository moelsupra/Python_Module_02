def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except (ValueError, TypeError):
        raise ValueError(
            f"Error: '{temp_str}' is not a valid number"
        )

    if temp > 40:
        raise ValueError(
            f"Error: {temp}°C is too hot for plants (max 40°C)"
        )
    if temp < 0:
        raise ValueError(
            f"Error: {temp}°C is too cold for plants (min 0°C)"
        )

    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for temp_str in tests:
        print(f"\nTesting temperature: {temp_str}")
        try:
            check_temperature(temp_str)
        except ValueError as e:
            print(e)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
