import csv
# Open and read the CSV file
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:

        print(" ".join(row))

#using string strip method
with open("student.csv", "r") as file:
    for line in file:
        print(line.strip())
#using Dictionaries
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"name: {row.get('name')}, ID: {row.get('ID')}, Marks: {row.get('Marks')}")