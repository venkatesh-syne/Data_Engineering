data = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 70}
]

total = 0

for item in data:
    total += item["marks"]

average = total / len(data)

print("Average:", average)