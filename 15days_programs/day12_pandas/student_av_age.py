import pandas as pd

df = pd.read_csv("students.csv")   # your file name

print(df['Age'].mean())