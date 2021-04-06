import requests
from bs4 import BeautifulSoup
import pandas as pd

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

df.to_excel("셀트리온시세02.xlsx")
print(df)