import csv
total_salary = 0
count = 0
with open("employee.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Reading employee data")

    for row in reader:
        print(row)
        # Convert salary to float and accumulate
        total_salary += float(row['Salary'])
        count += 1
        print("Total salary:", total_salary)
        print("Count:", count)
if count > 0:
    average_salary = total_salary / count
    print(f"Average salary: {average_salary}")
