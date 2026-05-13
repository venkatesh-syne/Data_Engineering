class Animal:

    def sound(self):
        print("Animal makes a sound")

# Derived class - Dog
class Dog(Animal):

    def sound(self):
        print("Dog barks")

# Derived class - Cat
class Cat(Animal):

    def sound(self):
        print("Cat meows")
# Example usage
d = Dog()
c = Cat()

d.sound()
c.sound()