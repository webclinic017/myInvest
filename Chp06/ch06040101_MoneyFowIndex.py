# ch06040101_MoneyFowIndex.py

import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB
import pandas as pd

mk = MarketDB()
df = mk.get_daily_price('NAVER', '2020-01-02')

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

print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06040101_MoneyFowIndex.xlsx')
