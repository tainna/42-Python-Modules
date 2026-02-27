
def check_temperature(temp_str: str) -> None:
    """
    Introduce the parameter in str bc everything
    that python recieve is str | "None" is bc the
    fucntion dont return nothing.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return
    if temp < 0:
        print(f"Error: {temp} is too cold for plants (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp} is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp} is perfect for plants!")


def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
