text = input("Enter a sentence: ")

# convert to lowercase
text = text.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for letter in alphabet:
    if letter not in text:
        is_pangram = False
        break

if is_pangram:
    print("It is a pangram")
else:
    print("It is not a pangram")
