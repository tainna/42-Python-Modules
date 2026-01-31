# The parent class for all garden errors
class GardenError(Exception):
    pass


# Specific errors (children of GardenError)
class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    # 1. Testing PlantError specifically
    print("Testing PlantError...")
    try:
        # We manually trigger the error with a message
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    # 2. Testing WaterError specifically
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # 3. Testing Inheritance (The "Catch-All" bucket)
    print("Testing catching all garden errors...")
    # Test A: PlantError caught as GardenError
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        # This works because PlantError IS A GardenError
        print(f"Caught a garden error: {e}")

    # Test B: WaterError caught as GardenError
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
