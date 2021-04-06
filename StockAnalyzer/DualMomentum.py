import sys
sys.path.append('./StockAnalyzer')
from Analyzer import MarketDB

import pandas as pd
# import pymysql



class DualMomentum:
    def __init__(self):
        """ 생성자: KRX 종목코드(codes)를 구하기 위한 MarketDB 객체 생성 """
        self.mk = MarketDB()

    def get_rltv_momentum(self, start_date, end_date, stock_count):
        """ 
        특정 기간 동안 수익률이 제일 높았던 stock_count 계약 종목들 (상대 모멘텀)
            - start_date  : 상대 모멘텀을 구할 시작일자(매수일) ('2020-01-01')
            - end_date    : 상대 모멘텀을 구할 종료일자(매도일) ('2020-12-01')
            - stock_count : 상대 모멘텀을 구할 종목수
        """

        df = self.mk.get_daily_price('삼성전자', start_date, end_date)
        myStartDate = df['date'].values[0]
        myEndDate = df['date'].values[(len(df)-1)]

        myRows = []
        myColumns = ['code', 'company', 'old_price', 'new_price', 'returns']

        # myCodes = {'000020': '동화약품', '000040': 'KR모터스'}

        for idx, myCode in enumerate(self.mk.codes):
        # for idx, myCode in enumerate(myCodes):
            df = self.mk.get_daily_price(myCode, start_date, end_date)
            if len(df) == 0:
                continue
            else:
                old_price = df['close'].values[0]
                new_price = df['close'].values[len(df)-1]

                myReturns = ((new_price / old_price) - 1) * 100
                myRows.append([myCode, self.mk.codes[myCode], old_price, new_price, myReturns])

                print(f"[{idx:04d}] [{myCode}] [{self.mk.codes[myCode]}] [{old_price}] [{new_price}] [{myReturns}]")

        df = pd.DataFrame(myRows, columns=myColumns)
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        df = df.sort_values(by='returns', ascending=False)
        df = df.head(stock_count)
        df.index = pd.Index(range(stock_count))

        print("\n------------------ df ------------------")
        print(df)
        print(f"\nRelative Momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}% \n")

        df.to_excel('.\\chp06\\ch06060400_TripleScreenTrading.xlsx')

        return df


    '''
    def get_rltv_momentum(self, start_date, end_date, stock_count):
        """ 
        특정 기간 동안 수익률이 제일 높았던 stock_count 계약 종목들 (상대 모멘텀)
            - start_date  : 상대 모멘텀을 구할 시작일자(매수일) ('2020-01-01')
            - end_date    : 상대 모멘텀을 구할 종료일자(매도일) ('2020-12-01')
            - stock_count : 상대 모멘텀을 구할 종목수
        """
        self.conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', charset='utf8')
        with self.conn.cursor() as curs:
            sql = f"SELECT max(date) FROM daily_price WHERE date <= '{start_date}'"
            curs.execute(sql)
            rs = curs.fetchone()
            if (rs[0] is None):
                return
            self.conn.commit()
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

        myRows = []
        myColumns = ['code', 'company', 'old_price', 'new_price', 'returns']

        myCodes = {'000020': '동화약품', '000040': 'KR모터스'}

        self.conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', charset='utf8')
        with self.conn.cursor() as curs:
            for _, myCode in enumerate(myCodes):
                sql = f"SELECT close FROM daily_price WHERE code='{myCode}' and date='{myStartDate}'"
                curs.execute(sql)
                myResult = curs.fetchone()
                self.conn.commit()
                if (myResult is None):
                    continue
                old_price = int(myResult[0])

                sql = f"SELECT close FROM daily_price WHERE code='{myCode}' and date='{myEndDate}'"
                curs.execute(sql)
                myResult = curs.fetchone()
                self.conn.commit()
                if (myResult is None):
                    continue
                new_price = int(myResult[0])

                myReturns = ((new_price / old_price) - 1) * 100
                myRows.append([myCode, self.mk.codes[myCode], old_price, new_price, myReturns])

        print(rows)

        self.conn.close()
        return
    '''

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
    dmt = DualMomentum()
    dmt.get_rltv_momentum('2020-10-15', '2021-03-16', 300)

