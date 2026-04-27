def write_sentences_to_file(sentences, file_path):
    # sentences: List of strings,    #file_path: Path to the output text file

    with open(file_path, 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')  # add newline after each sentence

# Example usage:
sentences_list = [
    "Python is fun.",
    "I love programming.",
    "File handling is easy.",
]
#calling function with 2 params
write_sentences_to_file(sentences_list, "output.txt")
print("Sentences have been written to output.txt")
with open("output.txt", 'r') as file:   #to check the content is available in the file
    print(file.read())