import json
class Customer:

    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def display(self):
        print(f"Name: {self.name}, Email: {self.email}, City: {self.city}")

customers = []
with open("customers.json", "r") as file:
    data = json.load(file)

    for item in data:
        cust = Customer(item["name"], item["email"], item["city"])
        customers.append(cust)

for cust in customers:
    cust.display()