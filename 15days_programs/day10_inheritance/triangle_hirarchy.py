# Base class
class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


# Derived class - Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Derived class - Triangle
class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


# Example usage
r = Rectangle(5, 3)
t = Triangle(3, 4, 5)

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())