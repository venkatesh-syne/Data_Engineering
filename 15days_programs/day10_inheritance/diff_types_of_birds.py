# Base class
class Animal:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal Name: {self.name}")


# Derived class - Bird
class Bird(Animal):

    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def display(self):
        print(f"Bird Name: {self.name}, Can Fly: {self.can_fly}")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying")
        else:
            print(f"{self.name} cannot fly")


# Derived class - Fish
class Fish(Animal):

    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type  # Freshwater / Saltwater

    def display(self):
        print(f"Fish Name: {self.name}, Water Type: {self.water_type}")

    def swim(self):
        print(f"{self.name} is swimming")


# Example usage
b = Bird("Parrot", True)
f = Fish("Goldfish", "Freshwater")

b.display()
b.fly()

f.display()
f.swim()
