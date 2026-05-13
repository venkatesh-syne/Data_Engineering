list1 = [1,2,3,4,5,6]
list2 = [5,2,3,4,7,8]
list3 = []
for item in list1:
    if item in list2:
        list3.append(item)
print(list3)