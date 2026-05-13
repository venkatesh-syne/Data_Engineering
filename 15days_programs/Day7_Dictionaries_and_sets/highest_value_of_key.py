data = [
    {"name": "A", "marks": 85,},
    {"name": "B", "marks": 75,},
    {"name": "C", "marks": 78,}
]

#key=lambda x: x["marks"] tells Python to compare using "marks"
highest = max(data, key=lambda x: x["marks"])
print(highest)

#This avoids errors if "marks" is missing
highest = max(data, key=lambda x: x.get("marks", 0))
print(highest)
