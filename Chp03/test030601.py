from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

myDow = pdr.get_data_yahoo('^DJI', start='2000-01-04')  # ①
myKospi = pdr.get_data_yahoo('^KS11', start='2000-01-04')  # ②

import matplotlib.pyplot as plt
plt.figure(figsize=(18, 7))
plt.plot(myDow.index, myDow.Close, 'r--', label="Dow Jones Industrial")  # ③
plt.plot(myKospi.index, myKospi.Close, 'b', label="KOSPI")  # ④
plt.grid(True)
plt.legend(loc='best')
plt.show()
