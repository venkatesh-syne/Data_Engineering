import pandas as pd

# Read JSON file
df = pd.read_json("data.json")

# Display full DataFrame
print(df)

# Extract specific column
print(df['Name'])

# Filter (example: maths > 70)
print(df[df['maths'] > 70])