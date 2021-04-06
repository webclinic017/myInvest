from pandas_datareader import data as pdr          # pip install pandas_datareader
import yfinance as yf                              # pip install yfinance

# yahoo Finance에 맞추어 Pandas Datareader를 재정의(override)한다.
yf.pdr_override()

# yahoo Finance로부터 DataFrame 형식으로 주식 Data 가져오기
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')

# msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

# for i in sec.index:
#     print(i, sec['Close'][i], sec['Volume'][i])

# print('\nhead(5)\n', sec.head())
# print('\ntail(5)\n', sec.tail())

# tmp_sec = sec.drop(columns='Volume')
# print("\n SEC DataFrame deleted Volume Column\n", tmp_sec)
# print(sec.index)

import matplotlib.pyplot as plt

plt.plot(sec.index, sec.Close, 'b', label="Samsung Electronics")
plt.legend(loc='best')
plt.show()
