# ch06040102_BollingerBand_TrendFollowing.py

import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

mk = MarketDB()
df = mk.get_daily_price('NAVER', '2020-01-02')

df['MA20'] = df['close'].rolling(window=20).mean()  # 20 이동평균선
df['stdev'] = df['close'].rolling(window=20).std()  # 20 표준편차
df['upper'] = df['MA20'] + (df['stdev'] * 2)        # Bollinger Band 상단
df['lower'] = df['MA20'] - (df['stdev'] * 2)        # Bollinger Band 하단
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower']) # %b(Percent B) 주가가 Bollinger Band의 어디에 있지는 그 위치를 알려주는 지표

df['TP'] = (df['high'] + df['low'] + df['close']) /3    # 중심가격(Typical Price)
df['PMF'] = 0
df['NMF'] = 0
for i in range(len(df.close)-1):
    if df.TP.values[i] < df.TP.values[i+1]:
        df.PMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]    # 긍정적 현금 흐름 (PMF: Positive Money Flow)
        df.NMF.values[i+1] = 0                                            # 부정적 현금 흐름 (NMF: Negative Money Flow)
    else:
        df.NMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
        df.PMF.values[i+1] = 0
df['MFR'] = df.PMF.rolling(window=10).sum() / df.NMF.rolling(window=10).sum()   # 현금흐름비율 (MFR: Money Flow Ratio)
df['MFI10'] = 100 - (100 / (1 + df['MFR']))    # 10일 기준 현금흐름비율(Money Flow Ratio 10)

df = df[19:]    # 맨 처음의 19개 요소는 20 이평값을 갖고 있지 않으므로, 무시하고, 20번째 요소를 첫번째 요소로 재지정한다.

print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06040102_BollingerBand_TrendFollowing.xlsx')

import matplotlib.pyplot as plt
plt.figure(figsize=(16, 8))

plt.subplot(2, 1, 1)
plt.title('NAVER Bollinger Band (20 Day, 2 std) - Trend Following')
plt.plot(df.index, df['close'], color='#0000ff', label='Close')   # 종가(close)를 그래프에 그린다.
plt.plot(df.index, df['upper'], 'r--', label='Upper Band')   # Bollinger Band의 상단 밴드를 그래프에 그린다.
plt.plot(df.index, df['MA20'], 'k--', label='Moving Average 20')   # Bollinger Band의 중간 밴드(20 이평선)를 그래프에 그린다.
plt.plot(df.index, df['lower'], 'c--', label='Lower Band')   # Bollinger Band의 하단 밴드를 그래프에 그린다.
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
for i in range(len(df.close)):
    if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
        plt.plot(df.index.values[i], df.close.values[i], 'r^')
    elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:
        plt.plot(df.index.values[i], df.close.values[i], 'bv')
plt.legend(loc='best')

plt.subplot(2, 1, 2)
plt.plot(df.index, df['PB'] * 100, 'b', label='%B x 100')
plt.plot(df.index, df['MFI10'], 'g--', label='MFI(10 day)')
plt.yticks([-20, 0, 20, 40, 60, 80, 100, 120])
for i in range(len(df.close)):
    if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
        plt.plot(df.index.values[i], 0, 'r^')
    elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:
        plt.plot(df.index.values[i], 0, 'bv')    
plt.grid(True)
plt.legend(loc='best')
plt.show()