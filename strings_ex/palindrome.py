word = input("Enter a word: ")
text = word[::-1]

if word == text:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
