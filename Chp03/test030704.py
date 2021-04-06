import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats                   # pip install scipy
import matplotlib.pyplot as plt

myDow = pdr.get_data_yahoo('^DJI', start='2000-01-04')
myKospi = pdr.get_data_yahoo('^KS11', start='2000-01-04')

df = pd.DataFrame({'X' : myDow['Close'], 'Y' : myKospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y)
regr_line = regr.intercept +  regr.slope * df.X
# regr_line = f'Y = {regr.intercept:.2f} +  {regr.slope:.2f} * X'


plt.figure(figsize=(7, 7))
# plt.plot(df.X, df.Y, marker='.')
plt.scatter(df.X, df.Y, marker='.')

plt.plot(df.X, regr_line, 'r')
plt.legend(['DOW x KOSPI Regression Line'])
plt.title(f'DOW X KOSPI (R= {regr.rvalue:.2f})')
plt.xlabel("Dow Jones Industrial Index")
plt.ylabel("KOSPI Index")

plt.show()

