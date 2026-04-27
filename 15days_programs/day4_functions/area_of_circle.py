import math

#Area=π×r2 π=3.14159
def circle_area(radius):
    """Calculate and return the area of a circle given its radius"""
    return math.pi * radius**2

# Example usage
radius = 5
area = circle_area(radius)
print("Area of the circle:", area)

import math  # to use math.pi

radius1 = 6
area = math.pi * radius1**2

print("Area of the circle:", area)