sentence = "hi this is python"

words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word, "has", len(longest_word), "letters")