import random

class Hat:
        
    houses = ["Grffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")

Hat.sort("Harry")