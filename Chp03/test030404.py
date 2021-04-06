from pandas_datareader import data as pdr
import yfinance as yf

# yahoo Finance에 맞추어 Pandas Datareader를 재정의(override)한다.
yf.pdr_override()

# yahoo Finance로부터 DataFrame 형식으로 주식 Data 가져오기
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

sec_dpc = ((sec['Close']/sec['Close'].shift(1))-1)*100
sec_dpc.iloc[0] = 0
sec_dpc.name = 'SEC_DPC'
sec_dpc_cs = sec_dpc.cumsum()

msft_dpc = ((msft['Close']/msft['Close'].shift(1))-1)*100
msft_dpc.iloc[0] = 0
msft_dpc.name = 'MSFT_DPC'
msft_dpc_cs = msft_dpc.cumsum()

import matplotlib.pyplot as plt

plt.plot(sec.index, sec_dpc_cs, 'b', label="Samsung Electronics")
plt.plot(msft.index, msft_dpc_cs, 'r--', label="Microsoft")
plt.ylabel("Change %")
plt.grid(True)
plt.legend(loc='best')
plt.show()