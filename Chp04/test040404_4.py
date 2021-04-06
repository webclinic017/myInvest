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

plt.plot(df.index, df.Close, 'b', label="Celtrion")
plt.legend(loc='best')
plt.show()
