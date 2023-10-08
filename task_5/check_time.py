import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
df.Date = pd.to_datetime(df.Date)
df = df.set_index('Date')
print(df.loc['2017', 'Close'].mean())

plt.plot(df.groupby('Date')['Open'].mean())
plt.savefig('apple.png')

