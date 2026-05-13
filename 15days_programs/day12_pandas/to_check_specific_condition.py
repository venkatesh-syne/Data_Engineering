import pandas as pd

def filter_dataframe(df, column_name, condition_value):
    return df[df[column_name] > condition_value]


df = pd.read_csv("students.csv")

filtered_df = filter_dataframe(df, "maths", 70)

print(filtered_df)