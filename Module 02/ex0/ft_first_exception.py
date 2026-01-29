
def check_temperature(temp_str: str) -> None:
    """
    Introduce the parameter in str bc everything
    that python recieve is str, the fucntion dont return
    nothing.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return
    if temp < 0:
        print(f"Error: {temp} is too cold for plants (mac 40°C)")
    elif temp > 40:
        print(f"Error: {temp} is too hot for plants (min 0°C)")
    else:
        print(f"Temperature {temp} is perfect for plants!")


def test_temperature_input() -> None:

    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    test_temperature_input()
