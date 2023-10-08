import pandas as pd

# my_series = pd.Series([2, 4, 6, 8, 10])
#
# print(my_series)
# print(my_series[1])
# print(my_series[4])


# my_series = pd.Series([2, 4, 6, 8, 10], index=['a', 'b', 'c', 'd', 'e'])
#
# print(my_series)
# print(my_series['c'])
# print(my_series['e'])

# my_series = pd.Series({'a': 1, 'b': 2, 'c': 3})

# print(my_series)
# print(my_series['a'])
# print(my_series['b'])

# print(my_series[['a', 'b']])
# my_series[['a', 'b']] = 10
# print(my_series)

# my_series_step_3 = pd.Series([1, 0, 2, -4, 3, 3.5, 4, 5, -7])
# print(my_series_step_3[my_series_step_3 >= 3])
# print(my_series_step_3[my_series_step_3 != -4])

# print(my_series_step_3.values)
# print(my_series_step_3.index)
# print(my_series_step_3.name)


def func(lst1, lst2):
    if len(lst1) == len(lst2):
        return pd.Series(lst1, index=lst2)
    else:
        raise ValueError('второй список не может использоваться в качетсве ключей для первого списка')

# print(func([1, 12, 3], [0]))

d = {'day_1': 300, 'day_2': 0, 'day_3': 400, 'day_4': 350}
# s = pd.Series(list(d.values())[:3], list(d.keys())[:3])
s = pd.Series(d, index=['day_1', 'day_2', 'day_3'])
print(s[s != 0])