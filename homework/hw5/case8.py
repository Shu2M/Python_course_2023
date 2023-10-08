from datetime import date
import pandas as pd


bct_usd = pd.read_csv('BCT-USD.csv')
date_min_volume = date.fromisoformat(bct_usd.loc[bct_usd['Volume'] == bct_usd['Volume'].min()]['Date'].values[0])
print(date_min_volume.strftime("%B"))
