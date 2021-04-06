from pandas_datareader import data as pdr
import yfinance as yf

# yahoo Finance에 맞추어 Pandas Datareader를 재정의(override)한다.
yf.pdr_override()

# yahoo Finance로부터 DataFrame 형식으로 주식 Data 가져오기
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')

sec_dpc = ((sec['Close']/sec['Close'].shift(1))-1)*100
sec_dpc.iloc[0] = 0
sec_dpc.name = 'DPC'

print(sec_dpc.describe())

import matplotlib.pyplot as plt
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show() 
