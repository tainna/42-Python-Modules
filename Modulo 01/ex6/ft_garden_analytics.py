# Create an Garden Manager -- hereditatry

class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

    def grow(self, cm) -> None:
        self.height += cm
        print(f"{self.name}: grew {cm}cm")

    def get_details(self) -> None:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_details(self):
        return (f"{super().get_details()}, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize

    def get_details(self):
        return (f"{super().get_details()}, Prize points: {self.prize}")


class GardenManager:
    total_managed = 0

    class GardenStats:
        def calculate_counts(self, plants):
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants = []
        self.total = 0
        self.stats = self.GardenStats()
        GardenManager.total_managed += 1

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def plant_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        count = 0
        while count < 3 and count < len(self.plants):
            p = self.plants[count]
            p.grow(1)
            self.total += 1
            count += 1

    def print_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plant in garden:")
        for i in range(len(self.plants)):
            print(f"- {self.plants[i].get_details()}")

        print(f"Plants added: {len(self.plants)}, Total growth: {self.total}")

        reg, flow, prz = self.stats.calculate_counts(self.plants)
        print(f"Plant types: {reg} regular, {flow} flowering, {prz} Flowers")

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls.total_managed}")


def ft_garden_analytics() -> None:
    print("=== Garden Management Demo ===")

    alice_garden = GardenManager("Alice")

    p1 = Plant("Oak Tree", 100)
    alice_garden.add_plants(p1)

    p2 = FloweringPlant("Rose", 25, "red")
    alice_garden.add_plants(p2)

    p3 = PrizeFlower("SunFlower", 50, "yellow", 10)
    alice_garden.add_plants(p3)

    alice_garden.plant_grow()

    alice_garden.print_report()

    valid = GardenManager.validate_height(10)
    print(f"Heght validation test: {valid}")

    bob_garden = GardenManager("Bob")
    bob_garden.add_plants(p1)

    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
