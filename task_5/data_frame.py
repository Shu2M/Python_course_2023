import pandas as pd


my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [121, 3121, 5454, 5454],
    'day_2': [5465, 65465, 654, 654],
    'day_3': [87, 987, 987, 987],
    'day_4': [654, 21, 5, 87],
})

print(my_df)
print()

my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [121, 3121, 5454, 5454],
    'day_2': [5465, 65465, 654, 654],
    'day_3': [87, 987, 987, 987],
    'day_4': [654, 21, 5, 87],
}, index=['B', 'M', 'P', 'C'])

print(my_df)
print()

print(my_df.loc['M'])
print()
print(my_df.iloc[1])
print()

print(my_df.loc[['B', 'M'], 'day_1'])
print()
print(my_df.loc[['B', 'M'], ['day_1', 'day_2']])
print()
print(my_df.loc['B':'M'])
print()
print(my_df.day_1)
print()
print(my_df['day_1'])
print()