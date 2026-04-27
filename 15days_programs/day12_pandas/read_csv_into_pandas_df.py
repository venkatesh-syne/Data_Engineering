import pandas as pd
test_data = pd.read_csv(r'C:\Users\vlsp1\PycharmProjects\project1\pandas_course\titanic\test.csv')
print(test_data)

# printing multiple columns
print(test_data[['Name', 'Age']])

# Age greater than 30
print(test_data[test_data['Age'] > 30])

# Only females
print(test_data[test_data['Sex'] == 'female'])

# Sort by Age
print(test_data.sort_values('Age'))

# Sort by Fare (descending)
print(test_data.sort_values('Fare', ascending=False))

#Add new column
test_data['Age_plus_10'] = test_data['Age'] + 10
print(test_data.head())
#Update values
test_data['Fare'] = test_data['Fare'] * 2

#Handle missing values
print(test_data.isnull().sum())

# Fill missing Cabin with 'Unknown'
test_data['Cabin'] = test_data['Cabin'].fillna('Unknown')

#Basic statistics
print(test_data['Age'].mean())
print(test_data['Fare'].max())

#Drop column
test_data = test_data.drop(columns=['Ticket'])

# Grouping
print(test_data.groupby('Sex')['Fare'].mean())