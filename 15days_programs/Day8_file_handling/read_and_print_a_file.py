file = open("test")
print(file.read())
file.close()
# using with keyword "with" will take care of your closing of your files.
with open("test") as file:
    print(file.read())
