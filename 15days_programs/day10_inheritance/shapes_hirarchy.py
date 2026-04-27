import math
# Base class
class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Triangle class (Heron's formula)
class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example usage
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 4, 5)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())