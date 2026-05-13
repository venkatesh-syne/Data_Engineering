def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))
print(even_odd(number))

