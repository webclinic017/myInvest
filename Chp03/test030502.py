from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
# import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', start='2004-01-04')

window = 252
peak = kospi['Close'].rolling(window, min_periods=1).max()
drawdown = kospi['Close']/peak - 1.0
max_dd = drawdown.rolling(window, min_periods=1).min()

max_dds = max_dd[max_dd == max_dd.min()]
print(max_dds)

'''
plt.figure(figsize=(18, 7))
plt.subplot(211)  # 2행 1열 중 1행에 그래프를 그린다.
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212)  # 2행 1열 중 2행에 그래프를 그린다.
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()
'''

