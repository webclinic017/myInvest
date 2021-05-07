# ch080203_test01.py
# pip install pywin32

import ctypes
import win32com.client as w32c
# CREON Plus 공통 Object
cpStatus = w32c.Dispatch('CpUtil.CpCybos')  # 시스템 상태 정보
cpTradeUtil = w32c.Dispatch('CpTrade.CpTdUtil')  # 주문 관련 도구

print("IsConnect : ", cpStatus.IsConnect)
print("ServerType : ", cpStatus.ServerType)
print("LimitRequestRemainTime : ", cpStatus.LimitRequestRemainTime)

print("TradeInit : ", cpTradeUtil.TradeInit(0))
