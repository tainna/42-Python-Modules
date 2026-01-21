class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")

    def set_height(self, cm: int) -> None:
        if cm < 0:
            print(f"Invalid operation attempted: height {cm}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = cm
            print(f"Height updated: {cm}cm [OK]")

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"Invalid operation attempted: age {days} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = days
            print(f"Age updated: {days} days [OK]")

    def get_height(self) -> None:
        return self._height

    def get_age(self) -> None:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    my_plant = SecurePlant("Rose")
    my_plant.set_height(25)
    my_plant.set_age(30)

    my_plant.set_age(-5)

    a = my_plant.get_age()
    h = my_plant.get_height()

    print(f"Current plant: {my_plant.name} ({h}cm, {a}days)")


if __name__ == "__main__":
    ft_garden_security()
