#Access a value using key.
student = {
    "name": "venkatesh",
    "age": 35
}
print(student["name"])


#Add a new key-value pair.
student["city"] = "Hyderabad"
print(student)

#Update a dictionary value.
student["age"] = 30
print(student)

#Delete a key from dictionary.
del student["age"]
print(student)

#Loop through dictionary keys and values.
for key, value in student.items():
    print(key, ":", value)

#Check if a key exists.
if "name" in student:
    print("Key exists")
else:
    print("Key not found")

#Print all keys from dictionary

print(student.keys())

#Print all values from dictionary

print(student.values())
