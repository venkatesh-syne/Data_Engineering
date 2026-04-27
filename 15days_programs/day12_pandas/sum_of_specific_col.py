import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# Calculate sum of a column (example: maths)
total = df['maths'].sum()

print("Sum of maths:", total)