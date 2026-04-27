def multiplication_table(n):

    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
print(multiplication_table(num))