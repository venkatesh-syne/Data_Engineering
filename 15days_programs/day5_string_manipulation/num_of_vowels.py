
text = input("Enter your name: ")
text =text.lower()
count = 0
for char in text:
    if char in "aeiou":
        count += 1
print(count)

#using functions
def count_vowels(text):
    text =text.lower()
    count = 0
    for char in text:
    	if char in "aeiou":
        	count += 1
    return count
text = input("Enter your name: ")
result = count_vowels(text)
print(result)

