num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")

elif num % 3 == 0:
    print(num, "is divisible only by 3")

elif num % 5 == 0:
    print(num, "is divisible only by 5")

else:
    print(num, "is not divisible by 3 or 5")