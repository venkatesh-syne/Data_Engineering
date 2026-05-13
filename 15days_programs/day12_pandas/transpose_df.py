import pandas as pd

def transpose_dataframe(df):
    return df.T

df = pd.read_csv("students.csv")

transposed_df = transpose_dataframe(df)

print(transposed_df)