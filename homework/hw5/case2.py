import pandas as pd
import numpy as np
import string


size = 10
index = list(string.ascii_uppercase[:size])
df = pd.DataFrame(np.random.randint(1, 10, size=(size, size)), index=index)
print(df)
print()

for letter in index:
    if df.loc[letter].all() > 5:
        print(df.loc[letter])
