"""#DAY 3: Control flow and loops
#Q 1: Write a program that checks if a given number is   positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("zero number")

#Q2.Create a loop that prints the first 10 even numbers.


#for i in range(1, 11):
 #   print(i * 2)

for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
#Q3: Implement a program that finds the largest number  in a list.
list1 = [1,2,3,4,5,6,7,8,9,10]
print(max(list1))

numbers = list(map(int, input("Enter a number separated with space: ").split()))
print(max(numbers))

#1.	Create a program that takes a year as input and checks if it is a leap year or not
year = int(input("Enter a year: "))

#it checks 2026 is divisible by 4 and not divisible by 100 or year is divisible by 400
#2026 % 4 = 506.5 so 1st condition fail and it wont go to next condition it exit if and go into else
if (year % 4 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

#2.	Given a list of integers, find all the even numbers and store them in a new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Empty list to store even numbers
even_numbers = []

# Loop through the list
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
#3.	Write a Python program to check if a given number is a prime number
# Take input from user
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

#5.	 Given a list of names, print all names starting with the letter 'A'
names = ["Alice", "Bob", "Arjun", "Anita", "John", "Alex"]

print("Names starting with 'A':")
for name in names:
    if name.startswith("A"):
        print(name)

# 6.	Implement a program that prints the multiplication table of a given number

num = int(input("Enter a number:"))
print("Multiplication Table of", num)

#here we are taking range of 10
for i in range(1, 6):
    #using fstring to print the table values
    print(f"{num} x {i} = {num * i}")

#7.	Write a program that calculates the factorial of a given number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
#8.	Create a loop that prints all prime numbers between 1 and 50

for num in range(2, 15):
    is_prime = True
    # Check if num is divisible by any number from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
#in single line
primes = [num for num in range(2, 51) if all(num % i != 0 for i in range(2, int(num**0.5)+1))]

print(primes)
#9.	Given a list of words, count the number of words with more than five characters
# Example list of words
words = ["apple", "banana", "cat", "elephant", "dog", "giraffe"]

# Using list comprehension to count words with more than 5 characters
count = sum(1 for word in words if len(word) > 5)

print("Number of words with more than 5 characters:", count)"""

#10.	Calculate the sum of digits of a given number
num = 12345  
sum_of_digits = 0

while num > 0:
    digit = num % 10         # Get the last digit
    sum_of_digits += digit   # Add it to the sum
    num = num // 10          # Remove the last digit

print("Sum of digits:", sum_of_digits)