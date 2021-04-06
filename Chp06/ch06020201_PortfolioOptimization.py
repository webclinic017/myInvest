# ch06020201_PortfolioOptimization.py
import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB
import pandas as pd
import numpy as np

mk = MarketDB()
myStocks = ['삼성전자', 'SK하이닉스', 'LG화학', 'NAVER']
df = pd.DataFrame()
for s in myStocks:
    df[s] = mk.get_daily_price(s, '2018-05-04', '2021-03-08')['close']

daily_ret = df.pct_change()            # 수익률, 성장률(Growth-Rate)
daily_ret = daily_ret.fillna(method='bfill')
daily_ret = daily_ret.fillna(method='ffill')
annual_ret = daily_ret.mean() * 252    # 연간 성장률

daily_cov = daily_ret.cov()            # 공분산(Covariance)
annual_cov = daily_cov * 252           # 연간 공분산

portfolio_ret = []           # 수익률 포트폴리오
portfolio_risk = []          # 리스크(위험도 분산) 포트폴리오
portfolio_weight = []        # 종목비중분산 포트폴리오
sharpe_ratio = []

for i in range(20000):
    myWeights = np.random.random(len(myStocks))
    myWeights /= np.sum(myWeights)

    myReturns = np.dot(myWeights, annual_ret)
    myRisks = np.sqrt(np.dot(myWeights.T, np.dot(annual_cov, myWeights)))

    portfolio_ret.append(myReturns)
    portfolio_risk.append(myRisks)
    portfolio_weight.append(myWeights)
    sharpe_ratio.append(myReturns/myRisks)

    print(f'[{i+1}] Calculated.....')

myPortfolio = {'Returns' : portfolio_ret, 'Risks' : portfolio_risk, 'Sharpes' : sharpe_ratio}
for idx, sName in enumerate(myStocks):
    myPortfolio[sName] = [weight[idx] for weight in portfolio_weight]

df = pd.DataFrame(myPortfolio)
df = df[['Returns', 'Risks', 'Sharpes'] + [s for s in myStocks]]

max_sharpe = df.loc[df['Sharpes'] == df['Sharpes'].max()]
min_risk = df.loc[df['Risks'] == df['Risks'].min()]

print("\n---------- df ----------")
print(df, '\n')
df.to_excel('.\\chp06\\ch06020201_PortfolioOptimization.xlsx')

print("\n---------- max_sharpe ----------")
print(max_sharpe, '\n')
print("\n---------- min_risk ----------")
print(min_risk, '\n')

import matplotlib.pyplot as plt
df.plot.scatter(x='Risks', y='Returns', c='Sharpes', cmap='viridis', edgecolors='k', figsize=(11, 7), grid=True)
plt.scatter(x=max_sharpe['Risks'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
plt.scatter(x=min_risk['Risks'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.title('Portfolio Optimization')
plt.xlabel('Risks')
plt.ylabel('Expected Returns')
plt.show()