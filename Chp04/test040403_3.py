from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

myUrl = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
myHeaders = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

req = Request(myUrl, headers=myHeaders)
webPage = urlopen(req).read()

with urlopen(Request(myUrl, headers=myHeaders)) as webDoc:
    webPage = BeautifulSoup(webDoc, 'lxml')
    pgrr = webPage.find('td', class_='pgRR')
#    print(pgrr.a['href'])
#    print(pgrr.prettify())
#    print(pgrr.text)
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]
    print(last_page)
