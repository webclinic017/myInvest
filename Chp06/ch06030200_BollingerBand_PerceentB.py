# ch06030200_BollingerBand_PerceentB.py
import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

mk = MarketDB()
df = mk.get_daily_price('NAVER', '2020-01-02')

df['MA20'] = df['close'].rolling(window=20).mean()  # 20 이동평균선
df['stdev'] = df['close'].rolling(window=20).std()  # 20 표준편차
df['upper'] = df['MA20'] + (df['stdev'] * 2)        # Bollinger Band 상단
df['lower'] = df['MA20'] - (df['stdev'] * 2)        # Bollinger Band 하단
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])  # %b(Percent B) 주가가 Bollinger Band의 어디에 있지는 그 위치를 알려주는 지표
df = df[19:]    # 맨 처음의 19개 요소는 20 이평값을 갖고 있지 않으므로, 무시하고, 20번째 요소를 첫번째 요소로 재지정한다.

print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06030200_BollingerBand_PerceentB.xlsx')

import matplotlib.pyplot as plt
plt.figure(figsize=(16, 8))

plt.subplot(2, 1, 1)
plt.plot(df.index, df['close'], color='#0000ff', label='Close')   # 종가(close)를 그래프에 그린다.
plt.plot(df.index, df['upper'], 'r--', label='Upper Band')   # Bollinger Band의 상단 밴드를 그래프에 그린다.
plt.plot(df.index, df['MA20'], 'k--', label='Moving Average 20')   # Bollinger Band의 중간 밴드(20 이평선)를 그래프에 그린다.
plt.plot(df.index, df['lower'], 'c--', label='Lower Band')   # Bollinger Band의 하단 밴드를 그래프에 그린다.
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
plt.title('NAVER Bollinger Band (20 Day, 2 std)')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.plot(df.index, df['PB'], color='b', label='%B')
plt.grid(True)
plt.legend(loc='best')
plt.show()