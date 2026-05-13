def list_intersection(list1, list2):
    # Using a list comprehension
    return [item for item in list1 if item in list2]

# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common_elements = list_intersection(list_a, list_b)
print("Intersection:", common_elements)