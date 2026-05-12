n = int(input("Enter n: "))
i = 1
product = 1

while i <= n:
    product *= i
    i += 1

print("Product:", product)