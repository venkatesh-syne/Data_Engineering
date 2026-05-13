"""a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum = a + b
print("a + b: ", sum)


f = float(input("Enter Celsius: "))
temp = f * 9/5 + 32
print(temp)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("total area is:",area)

name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"hello {name} you are {age} years old")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

#4.	Given a list of numbers, find the maximum and minimum values
#list = [4,6,10,2,14,12,20] hard coded list
numbers = list(map(int, input("Enter numbers separated by space: ").split())) #dynamic list
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

#5.	Create a Python function to check if a given string is a palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

text = input("Enter a word: ")

if is_palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
#6.	Calculate the compound interest for a given principal amount, interest rate, and time period

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    return ci

# Take input
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

ci = compound_interest(p, r, t)

print(f"Compound Interest: {ci}")
print(f"Total Amount: {p + ci}")
#7.	Write a program that converts a given number of days into years, weeks, and days
days = int(input("Enter number of days: "))

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print(years, "years,", weeks, "weeks,", remaining_days, "days")


def convert_days(total_days):
    years = total_days // 365
    remaining_days = total_days % 365

    weeks = remaining_days // 7
    days = remaining_days % 7

    return years, weeks, days

# Take input
total_days = int(input("Enter number of days: "))

years, weeks, days = convert_days(total_days)

print(f"{years} year(s), {weeks} week(s), {days} day(s)")
#9.	Create a program that takes a sentence as input and counts the number of words in it
sentence = input("Enter a sentence: ")
words = sentence.split()
count = len(words)
print(count)

# 10.Implement a program that swaps the values of two variables

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

def count_vowels(text):
    text =text.lower()
    count = 0
    for char in text:
    	if char in "aeiou":
        	count += 1
    return count
text = "venaktesh"
result = count_vowels(text)
print(result)
"""









