class Product:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = float(price)
        self.__quantity = int(quantity)

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Invalid quantity")

    def total_value(self):
        return self.__price * self.__quantity

    def display(self):
        print(f"Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}, Total: {self.total_value()}")


import json

products = []

with open("products.json", "r") as file:
    data = json.load(file)

    for item in data:
        p = Product(item["name"], item["price"], item["quantity"])
        products.append(p)

# Display products
for p in products:
    p.display()