# ch070603_Backtrader_RSI.py
from datetime import datetime
import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)
    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

cerebro = bt.Cerebro()
cerebro.addstrategy(MyStrategy)
data = bt.feeds.YahooFinanceData(dataname='036570.KS', fromdate=datetime(2017, 1, 1), todate=datetime(2021, 3, 24))
cerebro.adddata(data)
cerebro.broker.setcash(100000000)
cerebro.addsizer(bt.sizers.SizerFix, stake=30)

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()  # ⑧
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot()  # ⑨