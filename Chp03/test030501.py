from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')

sma20 = sec['Close'].rolling(window=20, min_periods=1).mean()

plt.figure(figsize=(18, 7))
plt.plot(sec.index, sec['Close'], 'b', label="Samsung Electronics")
plt.plot(sma20.index, sma20, 'r--', label="Simple Moving Average 20")
plt.grid(True)
plt.legend(loc='best')
plt.show()

