class Person:

    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age  # private attribute
    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Person("Venkatesh", 35)

print(p.get_name())
print(p.get_age())

p.set_age(40)
print(p.get_age())