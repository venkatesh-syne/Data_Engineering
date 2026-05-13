import json

def extract_employee_names(file_path):
    # Open the JSON file
    with open(file_path, 'r') as file:

    # Load JSON data into a Python dictionary
        data = json.load(file)

     # Extract employee names
    names = []
    for emp in data['employees']:
        names.append(emp['name'])
        names.append(emp['age'])
        names.append(emp['department'])
    return names

names_list = extract_employee_names("employee_data.json")
print("Employee Names:", names_list)