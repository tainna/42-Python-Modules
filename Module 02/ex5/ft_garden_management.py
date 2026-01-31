class GardenError(Exception):
    """Base class for garden errors."""
    pass


class PlantError(GardenError):
    """Error for plant-specific issues."""
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        """
        Adds a plant to the list.
        Raises PlantError if name is empty.
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """
        Waters all plants.
        Uses finally to ensure system closes.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        name: str,
        water: int,
        sun: int
    ) -> None:
        """
        Checks health parameters.
        Raises ValueError if invalid.
        """
        # Validate Water
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        elif water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")

        # Validate Sun
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
        elif sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()

    # 1. Adding Plants
    print("Adding plants to garden...")
    plants_to_add = ["tomato", "lettuce", ""]

    for plant in plants_to_add:
        try:
            manager.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    # 2. Watering Plants
    print("Watering plants...")
    manager.water_plants()

    # 3. Checking Health
    print("Checking plant health...")

    try:
        manager.check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    # 4. Error Recovery
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
