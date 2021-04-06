import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

import pymysql

class DualMomentum:
    def __init__(self):
        """ 생성자: KRX 종목코드(codes)를 구하기 위한 MarketDB 객체 생성 """
        print("__init__ OK")
        self.mk = MarketDB()

    def get_rltv_momentum1(self, start_date, end_date, stock_count):
        df = self.mk.get_daily_price('삼성전자', '2017-01-01')

        print(df)

    def get_rltv_momentum(self, start_date, end_date, stock_count):
        """ 
        특정 기간 동안 수익률이 제일 높았던 stock_count 계약 종목들 (상대 모멘텀)
            - start_date  : 상대 모멘텀을 구할 시작일자(매수일) ('2020-01-01')
            - end_date    : 상대 모멘텀을 구할 종료일자(매도일) ('2020-12-01')
            - stock_count : 상대 모멘텀을 구할 종목수
        """
        print("get_rltv_momentum OK")
        self.conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', charset='utf8')
        print("conn in get_rltv_momentum OK")
        with self.conn.cursor() as curs:
            print("with in get_rltv_momentum OK")
            sql = f"SELECT max(date) FROM daily_price WHERE date <= '{start_date}'"
            curs.execute(sql)
            print("execute1 in get_rltv_momentum OK")
            rs = curs.fetchone()
            if (rs[0] is None):
                print("start_date : {} -> returned None".format(sql))
                return
            self.conn.commit()
            print("commit1 in get_rltv_momentum OK")
            myStartDate = rs[0].strftime('%Y-%m-%d')

            sql = f"SELECT max(date) FROM daily_price WHERE date <= '{end_date}'"
            curs.execute(sql)
            rs = curs.fetchone()
            if (rs[0] is None):
                print("end_date : {} -> returned None".format(sql))
                return
            self.conn.commit()
            myEndDate = rs[0].strftime('%Y-%m-%d')

            print("Start Date :", myStartDate)
            print("End Date :", myEndDate)

        return

    def get_abs_momentum(self, rltv_momentum, start_date, end_date):
        """ 
        특정 기간 동안 상대 모멘텀에 투자했을 때의 평균 수익률 (절대 모멘텀)
            - rltv_momentum  : get_rltv_momentum() 함수의 리턴값 (상대 모멘텀)
            - start_date  : 절대 모멘텀을 구할 매수일 ('2020-01-01')
            - end_date    : 절대 모멘텀을 구할 매도일 ('2020-12-01')
        """
        ''' 중간 생략 '''
        return
       
if __name__ == '__main__':
    print("Start OK")
    dmt = DualMomentum()
    dmt.get_rltv_momentum1('2020-01-01', '2020-12-31', 1)

