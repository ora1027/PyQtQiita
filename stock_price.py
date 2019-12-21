import pandas as pd
import numpy as np
import requests
import json
import matplotlib
import matplotlib.pyplot as plt


class StockPrice:
    def __init__(self, df):
        self.start = 2015
        self.df_n225_last = df.loc[:'2015', 'Last']
        self.df_n225_last.plot(figsize=(15, 6), color="blue")
        self.calc_sma()
        self.df_n225_last['SMA'].plot(figsize=(15, 6), color="red")
        plt.show()

    def calc_sma(self):
        self.df_n225_last['SMA'] = self.df_n225_last.rolling(window=14).mean()


if __name__ == "__main__":
    API_TOKEN = 'ChwTtzwp4dD4JKoyaZ26'
    QUANDL_CODE = 'CHRIS/CME_NK2'

    # エンドポイントを定義する。
    url = f'https://www.quandl.com/api/v3/datasets/{QUANDL_CODE}/data.json?api_key={API_TOKEN}'

    # JSONデータを受け取り、JSONデータを辞書型に変えます。
    catched_response = requests.get(url)
    json_data = catched_response.json()

    # 列名リストと値リストを作る
    columns = json_data['dataset_data']['column_names']
    values = json_data['dataset_data']['data']

    # データフレームを作成します。日付('Date')をDataTimeIndexにします。
    df = pd.DataFrame(values, columns=columns)
    df.Date = pd.to_datetime(df.Date)
    df.set_index('Date', inplace=True)

    df.High.interpolate(inplace=True)
    df.Last = np.minimum(df.Last.interpolate(), df.High)
    df.Open.fillna(df.Last, inplace=True)
    df.Low = np.maximum(df.Low.interpolate(), df.Open)
    stock_price = StockPrice(df)
