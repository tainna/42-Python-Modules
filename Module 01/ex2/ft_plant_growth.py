class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

# To grow the Height
    def grow(self, cm: int) -> None:
        self.height += cm

# To grow the age
    def older(self) -> None:
        self.age += 1

# To return the string
    def info(self) -> None:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth() -> None:
    my_plant = Plant("Rose", 25, 30)

    print("=== Day 1 ==")
    print(my_plant.info())

    initial_height = my_plant.height

    for i in range(6):
        my_plant.grow(i)
        my_plant.older()

    print("=== Day 7 ===")
    print(my_plant.info())

    growth = my_plant.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
