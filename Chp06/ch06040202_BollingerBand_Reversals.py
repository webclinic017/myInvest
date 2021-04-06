# ch06040202_BollingerBand_Reversals.py

import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

mk = MarketDB()
df = mk.get_daily_price('SK하이닉스', '2018-11-01')

df['MA20'] = df['close'].rolling(window=20).mean()  # 20 이동평균선
df['stdev'] = df['close'].rolling(window=20).std()  # 20 표준편차
df['upper'] = df['MA20'] + (df['stdev'] * 2)        # Bollinger Band 상단
df['lower'] = df['MA20'] - (df['stdev'] * 2)        # Bollinger Band 하단
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower']) # %b(Percent B) 주가가 Bollinger Band의 어디에 있지는 그 위치를 알려주는 지표

df['II'] = ((2 * df['close'] - df['high'] - df['low']) / (df['high'] - df['low'])) * df['volume']  # Intraday Intensity (II) 지표
df['IIP21'] = (df['II'].rolling(window=21).sum() / df['volume'].rolling(window=21).sum()) * 100  # Intraday Intensity Percentage 21-days
df = df.dropna()

print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06040202_BollingerBand_Reversals.xlsx')

import matplotlib.pyplot as plt
plt.figure(figsize=(16, 8))

plt.subplot(3, 1, 1)
plt.title('SK Hynix Bollinger Band (20 Day, 2 std) - Reversals')
plt.plot(df.index, df['close'], color='m', label='Close')   # 종가(close)를 그래프에 그린다.
plt.plot(df.index, df['upper'], 'r--', label='Upper Band')   # Bollinger Band의 상단 밴드를 그래프에 그린다.
plt.plot(df.index, df['MA20'], 'k--', label='Moving Average 20')   # Bollinger Band의 중간 밴드(20 이평선)를 그래프에 그린다.
plt.plot(df.index, df['lower'], 'c--', label='Lower Band')   # Bollinger Band의 하단 밴드를 그래프에 그린다.
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9') # 밴드폭을 색으로 채운다.
for i in range(0, len(df.close)):
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        plt.plot(df.index.values[i], df.close.values[i], 'r^')
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        plt.plot(df.index.values[i], df.close.values[i], 'bv')
plt.legend(loc='best')

plt.subplot(3, 1, 2)
plt.plot(df.index, df['PB'], 'b', label='%b')
plt.grid(True)
plt.legend(loc='best')

plt.subplot(3, 1, 3)
plt.bar(df.index, df['IIP21'], color='g', label='II% 21day')
for i in range(0, len(df.close)):
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        plt.plot(df.index.values[i], 0, 'r^')
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        plt.plot(df.index.values[i], 0, 'bv')
plt.grid(True)
plt.legend(loc='best')
plt.show()