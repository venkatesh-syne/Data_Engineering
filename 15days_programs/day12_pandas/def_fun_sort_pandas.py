import pandas as pd

def sort_dataframe(df, column_name):
    return df.sort_values(by=column_name, ascending=True)

# Read CSV file
df = pd.read_csv("students.csv")

# Sort by Age
sorted_df = sort_dataframe(df, "Age")

print(sorted_df)