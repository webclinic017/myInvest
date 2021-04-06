# ch05_01_YahooFinance_SEC.py

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

df = pdr.get_data_yahoo('005930.KS', '2017-01-01')
print(df)

# 두개의 그래프 표시 영역 중 위는 SEC의 종가(Close)와 조정종가(Adj Close)를 표시하고, 아래는 SEC의 거래량(Volume)을 표시한다.
plt.figure(figsize=(18, 8))
plt.subplot(2, 1, 1)
plt.title("Samsung Electronics (Yahoo Finance)")
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(df.index, df['Close'], 'c', label='Close')
plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close')
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['Volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()
