# ch06070300_DualMomentum.py

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

        for idx, myCode in enumerate(self.mk.codes):
            df = self.mk.get_daily_price(myCode, start_date, end_date)
            if len(df) == 0:
                continue
            else:
                old_price = df['close'].values[0]
                new_price = df['close'].values[len(df)-1]

                myReturns = ((new_price / old_price) - 1) * 100
                myRows.append([myCode, self.mk.codes[myCode], old_price, new_price, myReturns])

                # print(f"[Relative Momentum] - [{idx:04d}] [{myCode}] [{self.mk.codes[myCode]}] [{old_price}] [{new_price}] [{myReturns}]")

        df = pd.DataFrame(myRows, columns=myColumns)
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        df = df.sort_values(by='returns', ascending=False)
        df = df.head(stock_count)
        df.index = pd.Index(range(stock_count))

        print(f"\n------------------ Relative Momentum df ({start_date} ~ {end_date}) ------------------")
        print(df)
        print(f"\nRelative Momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}% \n")

        df.to_excel('.\\chp06\\ch06070300_DualMomentum_RM.xlsx')

        return df

    def get_abs_momentum(self, rltv_momentum, start_date, end_date):
        """ 
        특정 기간 동안 상대 모멘텀에 투자했을 때의 평균 수익률 (절대 모멘텀)
            - rltv_momentum  : get_rltv_momentum() 함수의 리턴값 (상대 모멘텀)
            - start_date  : 절대 모멘텀을 구할 매수일 ('2020-01-01')
            - end_date    : 절대 모멘텀을 구할 매도일 ('2020-12-01')
        """
        
        stockList = list(rltv_momentum['code'])

        df = self.mk.get_daily_price('삼성전자', start_date, end_date)
        myStartDate = df['date'].values[0]
        myEndDate = df['date'].values[(len(df)-1)]

        myRows = []
        myColumns = ['code', 'company', 'old_price', 'new_price', 'returns']

        for idx, myCode in enumerate(stockList):
            df = self.mk.get_daily_price(myCode, start_date, end_date)
            if len(df) == 0:
                continue
            else:
                old_price = df['close'].values[0]
                new_price = df['close'].values[len(df)-1]

                myReturns = ((new_price / old_price) - 1) * 100
                myRows.append([myCode, self.mk.codes[myCode], old_price, new_price, myReturns])

                # print(f"[Absolute Momentum] - [{idx:04d}] [{myCode}] [{self.mk.codes[myCode]}] [{old_price}] [{new_price}] [{myReturns}]")

        df = pd.DataFrame(myRows, columns=myColumns)
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        df = df.sort_values(by='returns', ascending=False)

        print(f"\n------------------ Absolute Momentum df ({start_date} ~ {end_date}) ------------------")
        print(df)
        print(f"\nAbsolute Momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}% \n")

        df.to_excel('.\\chp06\\ch06070300_DualMomentum_AM.xlsx')

        return df

        return
       
if __name__ == '__main__':
    dmt = DualMomentum()
    rltvdf = dmt.get_rltv_momentum('2020-09-15', '2020-12-15', 300)
    dmt.get_abs_momentum(rltvdf, '2020-12-15', '2021-03-16')

