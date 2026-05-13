def union_lists(a, b):
    return list(set(a) | set(b))

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(union_lists(list1, list2))

#Without using set
def union_lists(a, b):
    result = []

    for i in a:
        if i not in result:
            result.append(i)

    for i in b:
        if i not in result:
            result.append(i)
    return result

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(union_lists(list1, list2))