# Mother class

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.n = name
        self.h = height
        self.a = age

    # Method to help format standard data
    def get_base_details(self):
        return f"{self.n}: {self.h}cm, {self.a} days"


# Kid Class
class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        # super() call o init of the class plant
        super().__init__(name, height, age)
        self.c = color

    def bloom(self) -> None:
        print(f"{self.n} is blooming beautifully!")


# There is another baby
class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diamter: int) -> None:
        super().__init__(name, height, age)
        self.diamet = trunk_diamter

# shade based on the exemple since 78/50 is 1,56
    def produce_shade(self) -> None:
        shade_area = int(self.diamet * 1.56)
        print(f"{self.n} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional: str) -> None:
        super().__init__(name, height, age)
        self.hseason = harvest_season
        self.nutritional_value = nutritional

    def show_nutrition(self):
        print(f"{self.n} is rich in {self.nutritional_value}")


# Main part
def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

# Creating lists to every type of plant to organize
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 35, 45, "white")
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 450, 1500, 40)
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 75, "winter", "vitamin A")
    ]
    # Now Flowers
    for i in range(2):
        f = flowers[i]
        # Access mother data (get_base_details) + kid data (color)
        print(f"{f.n} (Flower): {f.h}cm, {f.a} days, {f.c} color")
        f.bloom()

    # Now Trees
    for i in range(2):
        t = trees[i]
        print(f"{t.n} (Tree): {t.h}cm, {t.a} days, {t.diamet}cm diameter")
        t.produce_shade()

    # Vegetables
    for i in range(2):
        v = vegetables[i]
        print(f"{v.n} (Vegetable): {v.h}cm, {v.a} days, {v.hseason} harvest")
        v.show_nutrition()


if __name__ == "__main__":
    ft_plant_types()
