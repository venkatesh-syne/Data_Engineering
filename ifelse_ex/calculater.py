num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculater = input("Enter operator (+, -, *, /): ")

if calculater == "+":
    print("Result =", num1 + num2)

elif calculater == "-":
    print("Result =", num1 - num2)

elif calculater == "*":
    print("Result =", num1 * num2)

elif calculater == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero not possible")

else:
    print("Invalid operator")