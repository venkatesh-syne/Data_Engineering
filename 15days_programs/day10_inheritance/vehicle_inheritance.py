# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def display(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # Derived class - Car
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def display(self):
        print(f"Car Brand: {self.brand}, Doors: {self.doors}")

class Bike(Vehicle):  # Derived class - Bike

    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type  # e.g., Sports, Cruiser

    def display(self):
        print(f"Bike Brand: {self.brand}, Type: {self.type}")

c = Car("Toyota", 4)
b = Bike("Yamaha", "Sports")
c.display()
b.display()