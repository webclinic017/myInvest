from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
window=20
secSma20 = sec['Close'].rolling(window, min_periods=1).mean()
secMax = sec['Close'].rolling(window, min_periods=1).max()
secDrawdown = sec['Close']/secMax - 1.0
secMDD = secDrawdown.rolling(window, min_periods=1).min()

plt.figure(figsize=(18, 7))
plt.subplot(211)
sec['Close'].plot(label='SEC', title='SEC MDD', grid=True, legend=True)
plt.plot(secSma20.index, secSma20, 'r--', label="SMA20")
plt.subplot(212)
secDrawdown.plot(c='blue', label='SEC DD', grid=True, legend=True)
secMDD.plot(c='red', label='SEC MDD', grid=True, legend=True)
plt.show()

