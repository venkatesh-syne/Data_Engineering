import csv
# Initialize variables to track highest score and student name
highest_score = 1
top_student = ""

#Open the CSV file
with open("student1.csv", "r") as file:
    reader = csv.DictReader(file)  # Read CSV rows as dictionaries

    # Loop through each row
    for row in reader:   #Venkat,85 Nehan,90 preethi,65  ex: 85,90,65
        score = int(row["Score"])         # Convert the score from string to integer

        # Check if this score is higher than the current highest
        if score > highest_score:  #  1.85>-1  high score is 85 2.90>85 high score 90 3.65 > 90 false
            highest_score = score  # Update highest score
            top_student = row["Name"]  # Update top student's name
#Print the result
print("Top Student:", top_student)
print("Highest Score:", highest_score)
