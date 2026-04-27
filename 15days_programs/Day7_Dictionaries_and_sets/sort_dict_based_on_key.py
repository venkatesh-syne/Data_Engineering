def sort_dicts(data, key_name):
    return sorted(data, key=lambda x: x[key_name]) #reverse=True → descending order

data = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 92},
    {"name": "C", "marks": 78}
]

result = sort_dicts(data, "marks")
print(result)