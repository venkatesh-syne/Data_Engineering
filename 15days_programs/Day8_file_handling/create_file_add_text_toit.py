with open("myfile4.txt", "w") as file:
    file.write("Hello! This is python.\n")
    file.write("I am simple and easy to learn.")

print("File created and content written successfully.")

#Reading the myfile.txt
with open("myfile4.txt", "r") as file:
    print(file.read())
    print("File read successfully.")
