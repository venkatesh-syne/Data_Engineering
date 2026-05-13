import csv
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.total_value()}")
products = []

with open("products.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        name, price, quantity = row
        prod = Product(name, price, quantity)
        products.append(prod)

# Display all products
for p in products:
    p.display()