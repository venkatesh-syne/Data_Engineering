import math
# Base class
class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

# Derived class - Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Derived class - Square
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Example usage
c = Circle(3)
s = Square(4)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())
