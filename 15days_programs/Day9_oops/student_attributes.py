class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def information(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")

# Create object
details = Student("venkatesh", 35, "A")

# Call method
details.information()