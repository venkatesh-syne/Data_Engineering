text = "Python is very easy to learn"

words = text.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word is:", longest_word)