names = ["ram", "sita", "ram", "krishna", "sita"]
unique_names = list(set(names))  #using set method
print(unique_names)


fruits = ["mango", "apple", "mango", "apple", "kiwi"]
unique_names = []
for name in fruits:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)

