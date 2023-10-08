import pandas as pd
import numpy as np
import string


size = 10
index = list(string.ascii_uppercase[:size])
df = pd.DataFrame(np.random.random(size=(size, size)), index=index)
print(df)
print(df.shape)
print(df.columns.values)
print(df.to_numpy().mean())
df.to_csv('df.csv')
