# Open the file in read mode
with open("test", "r") as file:
    lines = file.readlines()  # Read all lines into a list

num_of_lines = len(lines) # Count lines

num_of_words = 0  # Count words
for line in lines:
    words_in_line = line.split()  # Split line into words
    print(words_in_line)
    num_of_words += len(words_in_line)  # Add number of words in this line
    print(num_of_words)

# Print results
print("Number of lines:", num_of_lines)
print("Number of words:", num_of_words)
