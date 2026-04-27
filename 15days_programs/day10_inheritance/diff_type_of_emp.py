# Base class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# Derived class - Manager
class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


# Derived class - Engineer
class Engineer(Employee):

    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

    def display(self):
        print(f"Engineer Name: {self.name}, Salary: {self.salary}, Skill: {self.skill}")


# Example usage
m = Manager("Venkatesh", 80000, "IT")
e = Engineer("Ravi", 60000, "Python")

m.display()
e.display()