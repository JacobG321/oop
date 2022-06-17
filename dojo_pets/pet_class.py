

class Pet:
    def __init__(self, name, type, tricks, noises):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.noises = noises
    
    def sleep(self):
        self.energy += 5
        print(f"+5 energy to {self.name}! Total energy is {self.energy}")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"+5 energy and +10 health to {self.name}! Total energy is {self.energy}, total health is {self.health}")

    def play(self):
        self.health += 5
        print(f"+5 health to {self.name}! Total health is {self.health}")

    def noise(self):
        print(self.noises)








