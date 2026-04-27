#Recursive Function
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

num = int(input("Enter the number: "))
print("Factorial:", factorial(num))

#without recursion
def _factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i   # multiply result by i
    return result
number = int(input("Enter the number: "))
print("Factorial:", factorial(number))