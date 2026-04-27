list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2 #+ → creates new list
print("result is:",result)

list1.extend(list2) #extend() → modifies existing list
print("updated list1:",list1)
