def reverse_string(text):
    text =text.lower()
    return text[::-1]
name = input("Enter your name: ")
print(reverse_string(name))