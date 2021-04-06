import requests
import pandas as pd
from bs4 import BeautifulSoup
import mplfinance as mpf

# 4.4.3 네이버 금융의 일별시세 테이블의 마지막 페이지가 몇 페이지인지 그 수자를 구한다.
myUrl = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
myHeaders = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

with requests.get(myUrl+'&page=1', headers=myHeaders) as req:
    webPage = BeautifulSoup(req.text, 'lxml')
    pgrr = webPage.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

# 4.4.4 일별 시세의 웹페이지에 있는 테이블 형태의 데이터 전체를 읽어서 DataFrame 객체(df)에 추가한다.
df = pd.DataFrame()
# for page in range(1, int(last_page)+1):
for page in range(1, 5):
    page_url = "{}&page={}".format(myUrl, page)
    with requests.get(page_url, headers=myHeaders) as req:
        dfPage = pd.read_html(req.text, encoding = 'euc-kr')[0]
    df = df.append(dfPage)
    print("page {} read".format(page))

# 4.5.3.2 Candle 차트 출력을 위한 데이터 재정비
df = df.dropna()
df = df.iloc[0:30]
df = df.rename(columns={'날짜': 'Date', '종가': 'Close', '전일비': 'Diff', '시가': 'Open', '저가': 'Low', '고가': 'High', '거래량': 'Volume'})
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# mplfinance 기반의 Candle Chart 그리기
kwargs = dict(title='Celltrion Candle Chart', type='candle', mav=(2, 4, 6), volume=True, ylabel='ohlc candle')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, **kwargs, style=s)
