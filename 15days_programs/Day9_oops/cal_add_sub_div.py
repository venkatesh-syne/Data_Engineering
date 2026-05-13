class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        result = a - b
        return f"subtraction of two numbers is {result}"

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
# self =calc  -->self represents the current object
calc = Calculator()
print(calc.add(5, 3))  # 8
print(calc.subtract(5, 3))  # 2
print(calc.multiply(5, 3))  # 15
print(calc.divide(5, 0))