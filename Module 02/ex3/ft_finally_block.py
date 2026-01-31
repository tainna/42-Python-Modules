from typing import List


def water_plants(plant_list: List[str]) -> None:
    # 1. Open the system
    print("Opening watering system")

    try:
        # 2. Iterate through the list provided in the argument
        for plant in plant_list:
            # Check if plant is valid (must be a string)
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")

            print(f"Watering {plant}")

    except Exception as error:
        # 3. Handle errors gracefully
        print(f"Error: {error}")

    finally:
        # 4. Cleanup: This always runs, ensuring the system closes
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    # Test 1: Normal List
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    # Test 2: List with an invalid item (None) to trigger error
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
