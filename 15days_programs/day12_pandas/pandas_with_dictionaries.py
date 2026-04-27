import pandas as pd
data = pd.DataFrame({'student_id':[101,102,103],'maths':[67,89,45],'science':[69,90,59]})
print(data)

print(data[['maths', 'science']])  #selecting 2 columns

# marks greater than 70 in maths and science
print(data[(data['maths'] > 70) & (data['science'] > 50)])

data['social'] = [56,67,39] #adding new column with values
