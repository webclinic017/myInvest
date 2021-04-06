import requests
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime

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

# 4.5.2 차트 출력을 위한 데이터 재정비
df = df.dropna()
df = df.iloc[0:30]
df = df.rename(columns={'날짜': 'Date', '종가': 'Close', '전일비': 'Diff', '시가': 'Open', '저가': 'Low', '고가': 'High', '거래량': 'Volume'})
df[['Close', 'Open', 'High', 'Low', 'Volume']] = df[['Close', 'Open', 'High', 'Low', 'Volume']].astype(int)

# 'Date' Column을 'datetime 형태가 아닌 Number 형태의 Data Type으로 변형해야 하며, DataFrame의 첫번째 Column으로 'Date', 그 다음으로 'Open', 'High', 'Low', 'Close' 순이어야 함
for idx in range(0, len(df)):
    dt = datetime.strptime(df['Date'].values[idx], '%Y.%m.%d').date()
    df['Date'].values[idx] = mdates.date2num(dt)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]
print(ohlc)

# 날짜 Index와, 종가 Column으로 차트 그리기
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
plt.title("Celltrion Candle Chart with mpl_finance")
candlestick_ohlc(ax, ohlc.values, width=0.7, colorup='red', colordown='blue')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.grid(color='gray', linestyle='--')
plt.show()
