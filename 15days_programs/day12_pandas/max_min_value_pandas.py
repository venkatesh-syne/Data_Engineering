import pandas as pd

df = pd.read_csv("students.csv")

print(df.max(numeric_only=True)) #numeric_only=True → ignores Name and grade
print(df.min(numeric_only=True))