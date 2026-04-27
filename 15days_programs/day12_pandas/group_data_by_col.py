import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

# Group by 'grade' and find mean of 'maths'
result = df.groupby('grade')['maths'].mean()

print(result)