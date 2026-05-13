import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius
# Create one object
c = Circle(5)

print("Area:", c.area())
print("Circumference:", c.circumference())

