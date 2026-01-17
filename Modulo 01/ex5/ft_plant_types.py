# Mother class

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    # Method to help format standard data
    def get_base_details(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

# Kid Class

class Flower(Plant): # Plant meas be the child of the mother Plant
    def __init__(self, name, height, age, color):
        #super() call o init of the class plant
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant): # There is another baby
    def __init__(self, name, height, age, trunk_diamter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diamter

    def produce_shade(self):
        #shade based on the exemple since 78/50 is 1,56
        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

# Main part

def ft_plant_types():
    print("=== Garden Plant Types ===")

    #Creating lists to every type of plant to organize 

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
        print(f"{f.name} (Flower): {f.height}cm, {f.age} days, {f.color} color")
        f.bloom()

    # Now Trees
    for i in range(2):
        t = trees[i]
        print(f"{t.name} (Tree): {t.height}cm, {t.age} days, {t.trunk_diameter}cm diameter")
        t.produce_shade()

    # Vegetables
    for i in range(2):
        v = vegetables[i]
        print(f"{v.name} (Vegetable): {v.height}cm, {v.age} days, {v.harvest_season} harvest")
        v.show_nutrition()

if __name__ == "__main__":
    ft_plant_types()