def garden_operations() -> None:

    print("Testing ValueError....")
    try:
        int('abc')
    except ValueError as error:
        print(f"Caught ValueError: {error}\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: no such file {error}\n")

    print("Testing KeyError...")
    try:
        data = {"Name": "Roses", "widht": 42, "age": 362}
        print(data["missing_plant"])
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")

    print("Testing multiple error together...")
    try:
        int("abc")
        data = {"Name": "Roses", "widht": 42, "age": 362}
        print(data["missing_plant"])
        10 / 0
        open("missing.txt")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!\n")


if __name__ == "__main__":
    test_error_types()
