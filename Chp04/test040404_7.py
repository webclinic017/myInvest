# 다음 금융 일봉 크롤링
import requests 
from bs4 import BeautifulSoup 
import json

url = 'https://finance.daum.net/api/charts/A066570/days?limit=200&adjusted=true' 
headers = { "referer": "https://finance.daum.net/chart/A005930", "user-agent": "Mozilla/5.0" } 
params = { "limit": "200", "adjusted": "true" } 
r = requests.get(url, headers=headers, params=params) 
szContent = r.text 
print (szContent) 

#soup = BeautifulSoup(html, 'html.parser') 
#titles = soup.select('span') 

str_list = [] 
list = json.loads(szContent) 
for price in list["data"]: 
    str_list.append(price["symbolCode"]) 
    str_list.append(" ") 
    str_list.append(price["date"]) 
    str_list.append(" : ") 
    str_list.append(str(price["tradePrice"]).replace(".0", "")) 
    str_list.append(" 원\n") 
print("".join(str(v) for v in str_list))