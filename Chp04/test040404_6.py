import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

myUrl = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
myHeaders = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

with requests.get(myUrl+'&page=1', headers=myHeaders) as req:
    webPage = BeautifulSoup(req.text, 'lxml')
    pgrr = webPage.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

df = pd.DataFrame()
for page in range(1, int(last_page)+1):
    page_url = "{}&page={}".format(myUrl, page)
    with requests.get(page_url, headers=myHeaders) as req:
        dfPage = pd.read_html(req.text, encoding = 'euc-kr')[0]
    
    df = df.append(dfPage)
    print("page {} read".format(page))

df = df.dropna()

df = df.rename(columns={'날짜': 'Date', '종가': 'Close', '전일비': 'Diff', '시가': 'Open', '저가': 'Low', '고가': 'High', '거래량': 'Volume'})
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.drop(['Diff'], axis=1)
df[['Close', 'Open', 'High', 'Low', 'Volume']] = df[['Close', 'Open', 'High', 'Low', 'Volume']].astype(int)

# ************************************************************** #
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dfy = pdr.get_data_yahoo('068270.KS', start='2005-07-19')

# ************************************************************** #
import FinanceDataReader as fdr

dff = fdr.DataReader('068270', '2005')

# ************************************************************** #
dfm = pd.DataFrame()

dfm = dfm.reindex(df.index)
dfm['NClose'] = df['Close']
dfm['YClose'] = dfy['Close']
dfm['FClose'] = dff['Close']

print(dfm)

df.to_excel("셀트리온시세11.xlsx")
dfy.to_excel("셀트리온시세12.xlsx")
dff.to_excel("셀트리온시세13.xlsx")

'''
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dfy = pdr.get_data_yahoo('068270.KS', start='2005-07-19')

plt.figure(figsize=(18, 7))
plt.plot(df.index, df.Close, 'b', label="Celtrion")
plt.plot(dfy.index, dfy.Close, 'b', label="Celtrion")
plt.show()
'''