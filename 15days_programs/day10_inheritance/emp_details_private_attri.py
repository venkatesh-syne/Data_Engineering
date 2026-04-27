class Employee:

    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = float(salary)

    # Getters
    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def display(self):
        print(f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}")


import csv

employees = []

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        name, position, salary = row
        emp = Employee(name, position, salary)
        employees.append(emp)

# Display employees
for emp in employees:
    emp.display()