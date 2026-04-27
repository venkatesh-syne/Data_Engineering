def check_word(sentence, word):
    if word in sentence:
        return "Word is present"
    else:
        return "Word is not present"

print(check_word("hi this is python", "python"))