#Area=1/2×base×height
def triangle_area(base, height):
     return 0.5 * base * height

    # Example usage
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))

area = triangle_area(b, h)
print("Area of the triangle:", area)