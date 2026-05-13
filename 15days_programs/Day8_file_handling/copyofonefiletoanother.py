with open("myfile.txt", "r") as src, open("myfile1.txt", "w") as dest:
    dest.write(src.read())

print("File copied successfully!")

#check wheather the file is copied or not.using read method.
with open("myfile1.txt", "r") as f:
    print(f.read())

#using for loop to copy the text line by line
with open("test", "r") as src, open("test1.txt", "w") as dest:
    for line in src:
        dest.write(line)
with open("test1.txt", "r") as f:
        print(f.read())
