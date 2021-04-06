# ch06060100_FirstScreen_inTripleScreenTrading.py

import pandas as pd
import datetime
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

mk = MarketDB()
df = mk.get_daily_price('엔씨소프트', '2017-01-01')

myEMA60 = df.close.ewm(span=60).mean()     # 종가의 12주(60거래일) 지수이동평균
myEMA130 = df.close.ewm(span=130).mean()   # 종가의 26주(130거래일) 지수이동평균
myMACD = myEMA60 - myEMA130                    # MACD
mySignal = myMACD.ewm(span=45).mean()        # 신호선(MACD의 9주 지수이동평균)
myMACDhist = myMACD - mySignal                 # MACD 히스토그램

df = df.assign(ema130=myEMA130, ema60=myEMA60, macd=myMACD, signal=mySignal, macdhist=myMACDhist).dropna()
df['number'] = df.index.map(mdates.date2num)   # 날짜 Type의 Data를 캔들차드에 사용할 수 있도록 숫자형 Data로 변환
myOHLC = df[['number', 'open', 'high', 'low', 'close']]

print("\n---------- myOHLC ----------")
print(myOHLC, '\n')
myOHLC.to_excel('.\\chp06\\ch06060100_FirstScreen_inTripleScreenTrading.xlsx')

plt.figure(figsize=(16, 8))

p1 = plt.subplot(2, 1, 1)
plt.title('Triple Screen Trading - First Screen (NCSOFT)')
plt.grid(True)
candlestick_ohlc(p1, myOHLC.values, width=.6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
plt.legend(loc='best')

p2 = plt.subplot(2, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Histogram')
plt.plot(df.number, df['macd'], color='b', label='MACD')
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
plt.legend(loc='best')

plt.show()