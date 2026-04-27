def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print(reverse_sentence("Hello World"))