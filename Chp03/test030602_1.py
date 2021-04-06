from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

myDow = pdr.get_data_yahoo('^DJI', start='2000-01-04') # ①
myDowRate = (myDow.Close / myDow.Close.loc['2000-01-04']) * 100
'''
myKospi = pdr.get_data_yahoo('^KS11', start='2000-01-04')
a1 = myKospi.loc['2000-01-04'].Close
b1 = myKospi.loc['2006-01-04'].Close
print(a1)
print(b1)
aa1 = (b1/a1) * 100
print(aa1)
myKospiRate = (myKospi.Close / myKospi.Close.loc['2000-01-04']) * 100
print(myKospiRate.loc['2000-01-05'])
'''
myKospiRate = (myKospi.Close / myKospi.Close.loc['2000-01-04']) * 100

import matplotlib.pyplot as plt
plt.figure(figsize=(18, 7))
plt.plot(myDowRate.index, myDowRate, 'r--', label="Dow Jones Industrial Rate")
plt.plot(myKospiRate.index, myKospiRate, 'b', label="KOSPI Rate")
plt.grid(True)
plt.legend(loc='best')
plt.show()
'''
