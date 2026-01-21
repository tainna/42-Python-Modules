class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_array() -> None:
    orders = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    print("=== Plant Factory Output ===")

    count = 0

    for i in range(5):
        current_order = orders[i]
        new = Plant(current_order[0], current_order[1], current_order[2])
        print(f"Created: {new.name} ({new.height}cm, {new.age} days)")
        count += 1

    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_array()
