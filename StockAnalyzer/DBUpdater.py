# Ch05_StockPriceAPI\Investar\DBUpdater.py
# SDA1\StockAnal\DBUpdater.py
import requests
import pandas as pd
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup
import json
import calendar
from threading import Timer
import re

class DBUpdater:
    def __init__(self):
        """ 생성자: MariaDB 연결 및 종목코드 Dictionary 생성 (ch5.3.4 참조) """
        self.conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', charset='utf8')
        with self.conn.cursor() as curs:
            sql = '''
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code)
            )
            '''
            curs.execute(sql)

            sql = '''
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date)
            )
            '''   
            curs.execute(sql)

        self.conn.commit()
        self.codes = dict()
        # self.update_comp_info()

    def __del__(self):
        """ 소멸자: MariaDB 연결 해제 """
        self.conn.close()

    def read_krx_code(self):
        """ KRX로부터 상장법인목록 파일을 읽어와서 DataFrame으로 반환 (ch4.1, ch5.3.5 참조) """
        # url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchTpe=13'
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
        krx = pd.read_html(url, header=0)[0]
        krx = krx[['종목코드', '회사명']]
        krx = krx.rename(columns={'종목코드' : 'code', '회사명' : 'company'})
        krx.code = krx.code.map('{:06d}'.format)

        return krx

    def update_company_info(self):
        """ 종목코드를 company_info 테이블에 업데이트한 후 Dictionary에 저장 (ch5.3.6 참조) """
        ''' 1) company_info Table의 last_update Column의 날짜 중 가장 최근 날짜가 없거나(한번도 기록 되지 않은 경우), 오늘보다 이전인 경우 '''
        ''' KRX 상장법인목록을 읽어서 company_info Table 전체를 Update한다. '''
        with self.conn.cursor() as curs:
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')
            
            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last_update) VALUES ('{code}', '{company}', '{today}')"
                    curs.execute(sql)
                    self.codes[code] =company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {(idx+1):04d} REPLACE INTO company_info VALUES ({code}, {company}, {today})")
                self.conn.commit()
                print('')

        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]] = df['company'].values[idx]

    def func_vjudfinm(self):
        
        return 

    def read_naver(self, code, company, pages_to_fetch, idx):
        """ 네이버 금융에서 주식 시세를 읽어서 DataFrame으로 반환 (ch4.4.3. 참조) """
        try:
            url = f"https://finance.naver.com/item/sise_day.nhn?code={code}"
            header = {'User-agent': 'Mozilla/5.0'}
            req = requests.get(url+'&page=1', headers=header)
            html = BeautifulSoup(req.text, "lxml")
            pgrr = html.find("td", class_='pgRR')
            if pgrr is None:
                return None
            s = str(pgrr.a["href"]).split('=')
            lastPage = s[-1]
            df = pd.DataFrame()
            pages = min(int(lastPage), pages_to_fetch)
            for page in range(1, pages+1):
                pg_url = '{}&page={}'.format(url, page)
                pg_req = requests.get(pg_url, headers={'User-agent': 'Mozilla/5.0'})
                pg_df = pd.read_html(pg_req.text, header=0)[0]
                df = df.append(pg_df)
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] [{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.format(tmnow, idx, company, code, page, pages), end="\n")
            df = df.rename(columns={'날짜':'date','종가':'close','전일비':'diff','시가':'open','고가':'high','저가':'low','거래량':'volume'})
            df['date'] = df['date'].replace('.', '-')
            df = df.dropna()
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
            df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
        except Exception as e:
            print('Exception occured :', str(e))
            return None
        return df        

    def replace_into_db(self, df, num, code, company):
        """ 네이버 금융에서 읽어온 주식 시세(read_naver())를 DB의 daily_price Table에 REPLACE (ch5.3.8 참조) """
        with self.conn.cursor() as curs:
            for idf in df.itertuples():
                sql = f"REPLACE INTO daily_price VALUES ('{code}', '{idf.date}', {idf.open}, {idf.high}, {idf.low}, {idf.close}, {idf.diff}, {idf.volume})"
                curs.execute(sql)
            self.conn.commit()

            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] #{(num+1):04d} {company} ({code}) : {len(df)} rows >>> REPLACE INTO daily_price [OK]")

    def update_daily_price(self, pages_to_fetch):
        """ KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트 """
        for idx, code in enumerate(self.codes):
            df = self.read_naver(code, self.codes[code], pages_to_fetch, idx+1)
            if df is None:
                continue
            self.replace_into_db(df, idx, code, self.codes[code])

    def execute_daily(self):
        """ 실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트 """
        self.update_company_info()

        '''
        try:
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        except FileNotFoundError:
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 1000
                config = {'pages_to_fetch': 1}
                json.dump(config, out_file)
        '''
        pages_to_fetch = 1
        self.update_daily_price(pages_to_fetch)

'''
        tmnow = datetime.now()
        lastDay = calendar.monthrange(tmnow.year, tmnow.month)[1]
        if tmnow.month == 12 and tmnow.day == lastDay:
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1, hour=17, minute=0, second=0)
        elif tmnow.day == lastDay:
            tmnext = tmnow.replace(month=tmnow.month+1, day=1, hour=17, minute=0, second=0)
        else:
            tmnext = tmnow.replace(day=tmnow.day+1, hour=17, minute=0, second=0)
        tmdiff = tmnext - tmnow
        secs = tmdiff.seconds

        t = Timer(secs, self.execute_daily)
        print("Waiting for next update ({})".format(tmnext.strftime('%Y-%m-%d %H:%M')))
        t.start()
'''

if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()
