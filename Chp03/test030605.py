from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

myDow = pdr.get_data_yahoo('^DJI', start='2000-01-04')
myKospi = pdr.get_data_yahoo('^KS11', start='2000-01-04')

import pandas as pd
df = pd.DataFrame({'DOW' : myDow['Close'], 'KOSPI' : myKospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

from scipy import stats
regr = stats.linregress(df['DOW'], df['KOSPI'])
print(regr)

X = df['DOW'].values
Y = regr.intercept +  regr.slope * X

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.plot(X, Y, 'r--', label="Linear Regression")
plt.xlabel("Dow Jones Industrial Index")
plt.ylabel("KOSPI Index")
plt.show()
