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
print("----- daily_ret -----")
print(daily_ret, '\n')

daily_ret = daily_ret.fillna(method='bfill')
daily_ret = daily_ret.fillna(method='ffill')
print("----- daily_ret -----")
print(daily_ret, '\n')

annual_ret = daily_ret.mean() * 252    # 연간 성장률
print("----- annual_ret -----")
print(annual_ret, '\n')

daily_cov = daily_ret.cov()            # 공분산(Covariance)
print("----- daily_cov -----")
print(daily_cov, '\n')
annual_cov = daily_cov * 252           # 연간 공분산
print("----- annual_cov -----")
print(annual_cov, '\n')

portfolio_ret = []           # 수익률 포트폴리오
portfolio_risk = []          # 리스크(위험도 분산) 포트폴리오
portfolio_weight = []        # 종목비중분산 포트폴리오

for _ in range(1):
    myWeights = np.random.random(len(myStocks))
    print("----- myWeights1 -----")
    print(myWeights, '\n')

    print("----- np.sum(myWeights) -----")
    print(np.sum(myWeights), '\n')
    myWeights /= np.sum(myWeights)
    print("----- myWeights2 -----")
    print(myWeights, '\n')

    myReturns = np.dot(myWeights, annual_ret)
    print("----- myReturns -----")
    print(myReturns, '\n')

    myRisks = np.sqrt(np.dot(myWeights.T, np.dot(annual_cov, myWeights)))
    print("----- myWeights.T -----")
    print(myWeights.T, '\n')
    print("----- np.dot(annual_cov, myWeights) -----")
    print(np.dot(annual_cov, myWeights), '\n')
    print("----- myRisks -----")
    print(myRisks, '\n')

    portfolio_ret.append(myReturns)
    portfolio_risk.append(myRisks)
    portfolio_weight.append(myWeights)

myPortfolio = {'Returns' : portfolio_ret, 'Risks' : portfolio_risk}
print("----- myPortfolio1 -----")
print(myPortfolio, '\n')

for idx, sName in enumerate(myStocks):
    myPortfolio[sName] = [weight[idx] for weight in portfolio_weight]
print("----- myPortfolio2 -----")
print(myPortfolio, '\n')
df = pd.DataFrame(myPortfolio)
df = df[['Returns', 'Risks'] + [s for s in myStocks]]
print("----- df -----")
print(df, '\n')