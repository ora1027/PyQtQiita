import sys
import os
from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

import pandas as pd
import numpy as np
import requests
import json

class Window(QtWidgets.QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)

        self.start = 2015
        self.df_n225_last = df.loc[:'2015', 'Last']
        self.df_n225_last.plot(figsize=(15, 6), color="blue")

        self.setWindowTitle("グラフ")
        self.setGeometry(300,300,800,500)

        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)

        self.canvas.move(200,20)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()

        self.button1 = QtWidgets.QPushButton('Plot',self)
        self.button1.clicked.connect(self.plot)
        self.button1.move(0,400)

        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setPlaceholderText("From Year")
        self.lineEdit1.move(0, 200)

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setPlaceholderText("To Year")
        self.lineEdit2.move(0, 300)

    def plot(self):
        ''' plot some random stuff '''
        self.calc_sma()
        data = [random.random() for i in range(25)]
        self.axes.plot(self.df_n225_last['SMA'], '*-')
        self.canvas.draw()


    def calc_sma(self):
        self.df_n225_last['SMA'] = self.df_n225_last.rolling(window=14).mean()


if __name__ == '__main__':
    API_TOKEN = 'ChwTtzwp4dD4JKoyaZ26'
    QUANDL_CODE = 'CHRIS/CME_NK2'

    url = f'https://www.quandl.com/api/v3/datasets/{QUANDL_CODE}/data.json?api_key={API_TOKEN}'
    # JSONデータを受け取り、辞書型に変換する。
    catched_response = requests.get(url)
    json_data = catched_response.json()

    # 列名リストと値リストを作成する。
    columns = json_data['dataset_data']['column_names']
    values = json_data['dataset_data']['data']

    # データフレームを作成する。
    df = pd.DataFrame(values, columns=columns)
    df.Date = pd.to_datetime(df.Date)
    df.set_index('Date', inplace=True)

    df.High.interpolate(inplace=True)
    df.Last = np.minimum(df.Last.interpolate(), df.High)
    df.Open.fillna(df.Last, inplace=True)
    df.Low = np.maximum(df.Low.interpolate(), df.Open)

    app = QtWidgets.QApplication(sys.argv)

    main = Window(df)
    main.show()

    sys.exit(app.exec_())
