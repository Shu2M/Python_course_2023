import pandas as pd
from datetime import date


bct_usd = pd.read_csv('BCT-USD.csv')
month = list()

for series in bct_usd.itertuples():
    if series.Open < series.Close:
        month.append((date.fromisoformat(series.Date).strftime("%B")))

if not month:
    print('Месяцев нет')
else:
    print(set(month))

