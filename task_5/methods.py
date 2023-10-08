import pandas as pd

my_df = pd.DataFrame({
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_1': [121, 3121, 5454, 5454],
    'day_2': [5465, 65465, 654, 654],
    'day_3': [87, 987, 987, 987],
    'day_4': [654, 21, 5, 87],
}, index=['B', 'M', 'P', 'C'])


my_df_step2 = pd.DataFrame({
    'day_1': [121, 3121, 5454, 5454],
    'product': ['bread', 'milk', 'potato', 'candies'],
    'day_2': [5465, 65465, 654, 654],
    'day_3': [87, 987, 987, 987],
    'day_4': [654, 21, 5, 87],
}).set_index('product')

print(my_df_step2)
print()

# my_df_step2 = my_df_step2.reset_index()
# print(my_df_step2)
# print()

my_df_step2 = my_df_step2.rename(columns={'day_1': 'day_01'})
my_df_step2 = my_df_step2.rename({'bread': 'bread_01'})
print(my_df_step2)
print()


my_df_step2['sum'] = my_df_step2.sum(axis=1)
print(my_df_step2)
print()

my_df_step2 = my_df_step2.drop(['day_4'], axis='columns')
my_df_step2 = my_df_step2.drop('candies')
print(my_df_step2)
print()


data_set = pd.DataFrame({
    'id': [0, 1, 2, 3],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 9, 3, 1],
    'dep_time': [517, 533, 542, 544],
    'sched_dep_time': [515, 529, 540, 545],
}).set_index('id')

print(data_set)
print(data_set.loc[data_set.month == 1])

data_set['diff'] = data_set.dep_time - data_set.sched_dep_time

print(data_set)
