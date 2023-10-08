import pandas as pd
import matplotlib.pyplot as plt


def func(start_date: str, stop_date: str) -> None:
    bct_usd = pd.read_csv('BCT-USD.csv')
    date_range_df = bct_usd.loc[(bct_usd['Date'] >= start_date) & (bct_usd['Date'] <= stop_date)]

    plt.plot(date_range_df['Open'])
    plt.savefig('open.png')

    plt.clf()

    plt.plot(date_range_df['Close'])
    plt.savefig('close.png')


func('2021', '2022')



