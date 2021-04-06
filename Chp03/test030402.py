from pandas_datareader import data as pdr
import yfinance as yf

# yahoo Finance에 맞추어 Pandas Datareader를 재정의(override)한다.
yf.pdr_override()

# yahoo Finance로부터 DataFrame 형식으로 주식 Data 가져오기
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

print(sec)

sec_dpc = ((sec['Close']/sec['Close'].shift(1))-1)*100
sec_dpc.iloc[0] = 0

msft_dpc = ((msft['Close']/msft['Close'].shift(1))-1)*100
msft_dpc.iloc[0] = 0

print("\nSamsung Electronics Daily Percent Change Rate")
print(sec_dpc.head())

print("\nMicrosoft Daily Percent Change Rate")
print(msft_dpc.head())

import pandas as pd 
sec_df = pd.DataFrame(sec_dpc['Close'], columns='DPC')
print("\nSamsung Electronics DataFrame")
print(sec_df)