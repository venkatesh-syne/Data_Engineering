import pandas as pd

dates = pd.date_range(start='2023-01-01', periods=5)

s = pd.Series(dates)
print(s)

filtered = s[(s >= '2023-01-03') & (s <= '2023-01-06')]
print(filtered)