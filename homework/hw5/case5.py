import pandas as pd
import matplotlib.pyplot as plt


emojis = pd.read_csv('emojis.csv')

plt.plot(emojis.groupby('Year')['Emoji'].count())
plt.savefig('emojis.png')
