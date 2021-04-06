from django.shortcuts import render
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_data(stock_code):
    myUrl = f'https://finance.naver.com/item/sise.nhn?code={stock_code}'
    myHeaders = {'user-agent' : 'Mozilla/5.0'}
    with urlopen(Request(myUrl, headers=myHeaders)) as webDoc:
        webPage = BeautifulSoup(webDoc, 'lxml', from_encoding="euc-kr")
        cur_price = webPage.find('strong', id='_nowVal')  # ①
        cur_rate = webPage.find('strong', id='_rate')  # ②
        stock = webPage.find('title')  # ③
        stock_name = stock.text.split(':')[0].strip()  # ④
        return cur_price.text, cur_rate.text.strip(), stock_name

def mainview(request):
    querydict = request.GET.copy()
    myList = querydict.lists()  # ⑤

    rows = []
    total = 0
    for x in myList:
        cur_price, cur_rate, stock_name = get_data(x[0])   # ⑥
        cprice = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',')   # ⑦
        sum = int(cprice) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum]) # ⑧
        total = total + int(cprice) * int(x[1][0])   # ⑨
        
    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount}  # ⑩

    return render(request, 'balance.html', values)  # ⑪

