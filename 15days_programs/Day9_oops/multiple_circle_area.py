import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius
# List of radii
radii = [2, 3, 5]

circles = []
# Create objects
for r in radii:
    circles.append(Circle(r))

# Display results
for c in circles:
    print(f"Radius: {c.radius}")
    print(f"Area: {c.area()}")
    print(f"Circumference: {c.circumference()}")
