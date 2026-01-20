# Create an Garden Manager -- hereditatry

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name}: grew {cm}cm")
    
    def get_details(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height) #Call the mother Plant
        self.color = color
    
    def get_details(self):
        return(f"{super().get_details()}, {self.color} flowers (blooming)")
    
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize
    
    def get_details(self):
        return(f"{super().get_details()}, Prize points: {self.prize}")

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
            
            return f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers"
    
    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants = []
        self.total_growth_tracker = 0
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
            self.total_growth_tracker += 1
            count += 1
    
    def print_report(self):
        
        