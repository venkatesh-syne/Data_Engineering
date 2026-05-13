def numbers_in_file(filepath):
    total = 0

    with open(filepath, 'r') as file:
       for line in file:
        line = line.strip()  #removes whitespaces
        print(line)
        if line != '':  # ignore empty lines
            total += float(line)  # convert each line to a number
            print("Running total:", total)

    return total
# Call the function and print the result
result = numbers_in_file(r"/Day8_file_handling\numbers")
print("Sum of numbers:", result)