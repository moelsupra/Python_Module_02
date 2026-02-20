def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", 'r')
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        dic = {"flower": 50, "oak": 40}
        print(dic["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    ft_different_errors()
    print("All error types tested successfully!")


if __name__ == "__main__":  # Entry-point check
    test_error_types()

# Catch a base exception class
# try:
#     pass
# except Exception as e:
#     print(f"Error: {e}")
