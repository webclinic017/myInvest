# ch06010203_EfficientFontier.py
import sys
sys.path.append('./StockAnalyzer')
import pandas as pd
import numpy as np
from Analyzer import MarketDB

mk = MarketDB()
myStocks = ['삼성전자', 'SK하이닉스', 'LG화학', 'NAVER']
df = pd.DataFrame()

for s in myStocks:
    df[s] = mk.get_daily_price(s, '2018-05-04', '2021-03-05')['close']

daily_ret = df.pct_change()            # 수익률, 성장률(Growth-Rate)
daily_ret = daily_ret.fillna(method='bfill')
daily_ret = daily_ret.fillna(method='ffill')
annual_ret = daily_ret.mean() * 252    # 연간 성장률

daily_cov = daily_ret.cov()            # 공분산(Covariance)
annual_cov = daily_cov * 252           # 연간 공분산

portfolio_ret = []           # 수익률 포트폴리오
portfolio_risk = []          # 리스크(위험도 분산) 포트폴리오
portfolio_weight = []        # 종목비중분산 포트폴리오

for i in range(20000):
    myWeights = np.random.random(len(myStocks))
    myWeights /= np.sum(myWeights)

    myReturns = np.dot(myWeights, annual_ret)
    myRisks = np.sqrt(np.dot(myWeights.T, np.dot(annual_cov, myWeights)))

    portfolio_ret.append(myReturns)
    portfolio_risk.append(myRisks)
    portfolio_weight.append(myWeights)

    print(f'[{i+1}] Calculated.....')

myPortfolio = {'Returns' : portfolio_ret, 'Risks' : portfolio_risk}
for idx, sName in enumerate(myStocks):
    myPortfolio[sName] = [weight[idx] for weight in portfolio_weight]

df = pd.DataFrame(myPortfolio)
df = df[['Returns', 'Risks'] + [s for s in myStocks]]
print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06010203_EfficientFontier.xlsx')

import matplotlib.pyplot as plt
df.plot.scatter(x='Risks', y='Returns', figsize=(10, 7), grid=True)
plt.title('Efficient Frontier')
plt.xlabel('Risks')
plt.ylabel('Expected Returns')
plt.show()