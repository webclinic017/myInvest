# Ch05_MarketDB API ch5.4 참조
# SDA1\StockAnal\MarketDB.py
import pymysql, re
import pandas as pd
from datetime import datetime, timedelta

class MarketDB:
    def __init__(self):
        """ 생성자: MariaDB 연결 및 종목코드 Dictionary 생성 (ch5.3.4 참조) """
        self.conn = pymysql.Connect(host='localhost', user='root', password='2543', db='stockdb', charset='utf8')
        self.codes = {}
        self.get_company_info()

    def __del__(self):
        """ 소멸자: MariaDB 연결 해제 """
        self.conn.close()

    def get_company_info(self):
        """ naverstock DB 내의 company_info Table에서 Data를 읽어와서 codes Dictionary (종목코드, 종목명)에 저장 """
        sql ="SELECT * FROM company_info"
        krx = pd.read_excel(sql, self.conn)
        for idx in range(len(krx)):
            self.codes[krx['code'].values[idx]] = krx['company'].values[idx]

    def get_daily_price(self, code, start_date, end_date):
        """ KRX 종목별 시세를 DataFrame 형태로 반환
            - code       : KRX 종목코드(예: '005930') 또는 상장기업명(예: '삼성전자'))
            - start_date : 조회 시작일('2021-01-01'), 미입력시 1년전 오늘 날짜 지정
            - end_date   : 조회 종료일('2021-01-01'), 미입력시 오늘 날짜 지정
        """
        sql = f"SELECT * FROM daily_price WHERE code='{code}' and date >= '{start_date}' and date <= '{end_date}'"
        df = pd.read_excel(sql, self.conn)
        df.index = df['date']
        return df
