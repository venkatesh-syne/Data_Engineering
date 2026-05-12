num = int(input("Enter a number:"))
print("Multiplication Table of", num)

#here we are taking range of 10
for i in range(1, 6):
    #using fstring to print the table values
    print(f"{num} x {i} = {num * i}")
