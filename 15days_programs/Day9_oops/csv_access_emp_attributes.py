import csv
class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

employees = []
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        name, position, salary = row
        emp = Employee(name, position, salary)
        employees.append(emp)

for emp in employees:
    emp.display()