import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def func(category_name: str) -> None:
    emojis = pd.read_csv('emojis.csv')
    if category_name in emojis['Category'].values:
        all_emojis = emojis.groupby('Category')['Emoji'].count()
        print(f'{category_name}: {all_emojis[category_name] / all_emojis.sum() * 100} %')
    else:
        print(f'Введенная категория "{category_name}" отсутствует в наборе данных')


func('noname')
func('Flags')
