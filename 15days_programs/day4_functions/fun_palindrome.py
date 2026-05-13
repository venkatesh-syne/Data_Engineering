def palindrome(string):
    return string == string[::-1]

name = input("Enter a string: ")
if palindrome(name):
    print("the entered string is Palindrome")
else:
    print("the entered string is Not a palindrome")
