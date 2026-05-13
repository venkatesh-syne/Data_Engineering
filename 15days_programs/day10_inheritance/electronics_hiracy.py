# Base class
class Electronics:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Price: {self.price}")


# Derived class - Phone
class Phone(Electronics):

    def __init__(self, brand, price, camera_mp, battery_mah):
        super().__init__(brand, price)
        self.camera_mp = camera_mp
        self.battery_mah = battery_mah

    def display(self):
        print(
            f"Phone -> Brand: {self.brand}, Price: {self.price}, Camera: {self.camera_mp}MP, Battery: {self.battery_mah}mAh")


# Derived class - Laptop
class Laptop(Electronics):

    def __init__(self, brand, price, ram, processor):
        super().__init__(brand, price)
        self.ram = ram
        self.processor = processor

    def display(self):
        print(f"Laptop -> Brand: {self.brand}, Price: {self.price}, RAM: {self.ram}GB, Processor: {self.processor}")
# Example usage
p = Phone("Samsung", 30000, 64, 5000)
l = Laptop("Dell", 60000, 16, "Intel i7")

p.display()
l.display()