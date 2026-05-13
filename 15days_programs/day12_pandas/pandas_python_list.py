import pandas as pd

profit= pd.Series([75, 80, 66], index = ['2018 Profit', '2019 Profit', '2020 Profit'])
#print(profit)

check_profit = profit[profit > 78] #filtering the dat based on condition
print(check_profit)

#sorting values based on data values
sorted_list = profit.sort_values()
print(sorted_list)