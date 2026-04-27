import pandas as pd

def add_calculated_column(df):

    df['total'] = df['maths'] + df['science'] + df['social']
    return df


df = pd.read_csv("students.csv")

df = add_calculated_column(df)
print(df)