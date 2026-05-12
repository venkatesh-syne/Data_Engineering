lst = [12, 45, 7, 89, 34]

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest number:", largest)