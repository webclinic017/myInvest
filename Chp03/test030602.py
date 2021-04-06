from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

myDow = pdr.get_data_yahoo('^DJI', start='2000-01-04')
myDowRate = (myDow.Close / myDow.Close.loc['2000-01-04']) * 100    # ①
myKospi = pdr.get_data_yahoo('^KS11', start='2000-01-04')
myKospiRate = (myKospi.Close / myKospi.Close.loc['2000-01-04']) * 100   # ②

import matplotlib.pyplot as plt
plt.figure(figsize=(18, 7))
plt.plot(myDowRate.index, myDowRate, 'r--', label="Dow Jones Industrial Rate")
plt.plot(myKospiRate.index, myKospiRate, 'b', label="KOSPI Rate")
plt.grid(True)
plt.legend(loc='best')
plt.show()
