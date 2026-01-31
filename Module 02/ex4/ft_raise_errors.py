def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    # 1. Check Name: "if not" catches empty strings "" AND None
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    # 2. Check Water (Must be 1 to 10)
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    # 3. Check Sunlight (Must be 2 to 12)
    elif sunlight_hours > 12:
        # We create a variable 'msg' to keep the line short for flake8
        msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        raise ValueError(msg)
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    # 4. Success: If no errors were raised, this line runs
    else:
        return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    # Test 1: Good values
    print("Testing good values...")
    try:
        # We capture the success message in a variable and print it
        result = check_plant_health("tomato", 5, 6)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 2: Empty plant name
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 3: Bad water level
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 4: Bad sunlight hours
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
