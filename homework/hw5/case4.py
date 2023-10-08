import pandas as pd
import numpy as np


emojis = pd.read_csv('emojis.csv')
print(emojis.loc[emojis.Rank == 1, 'Subcategory'])
