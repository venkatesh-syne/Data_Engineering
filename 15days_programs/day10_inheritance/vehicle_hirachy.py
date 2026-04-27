# Base class
class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")


# Derived class - Car
class Car(Vehicle):

    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def display(self):
        print(f"Car -> Brand: {self.brand}, Speed: {self.speed}, Doors: {self.doors}")


# Derived class - Bike
class Bike(Vehicle):

    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type  # Sports, Cruiser

    def display(self):
        print(f"Bike -> Brand: {self.brand}, Speed: {self.speed}, Type: {self.type}")


# Derived class - Truck
class Truck(Vehicle):

    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity  # load capacity

    def display(self):
        print(f"Truck -> Brand: {self.brand}, Speed: {self.speed}, Capacity: {self.capacity}")


# Example usage
c = Car("Toyota", 180, 4)
b = Bike("Yamaha", 120, "Sports")
t = Truck("Tata", 100, "10 Tons")

c.display()
b.display()
t.display()