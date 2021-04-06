# Ch05_StockPriceAPI\Investar\DBUpdater.py
# SDA1\StockAnal\DBUpdater.py
import requests
import pandas as pd
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup

class DBUpdater:
    def __init__(self):
        self.codes = dict()

    def update_company_info(self):
        self.codes['1111'] = 'aaaa'
        self.codes['2222'] = 'bbbb'
        self.codes['3333'] = 'cccc'
        self.codes['4444'] = 'eeee'

        # print(self.codes)

    def read_naver(self):
        """ 네이버 금융에서 주식 시세를 읽어서 DataFrame으로 반환 (ch4.4.3. 참조) """
        for idx, code in enumerate(self.codes):
            print('idx={:06d}, code={:10s}, name={:20s}'.format(idx, code, self.codes[code]))

if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.update_company_info()
    print(dbu.codes)
    dbu.read_naver()
