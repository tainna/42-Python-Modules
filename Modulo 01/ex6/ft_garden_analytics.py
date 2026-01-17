# Create an Garden Manager -- hereditatry

class Plant:
    def __init__(self, name, height)
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

    
