# ch080203_etfalgotrader.py
import ctypes
import win32com.client
import requests
import json
from datetime import datetime

def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), message)

    SLACK_BOT_TOKEN = "xoxb-1892258795171-1906429068097-YeoZUcKTm8ZwtantfeCj99Z7"
    myHeaders = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
        }

    myChannel = '#trading'
    myText = datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ') + message
    myPayload = {
        'channel': myChannel,
        'text': myText
        }
    r = requests.post('https://slack.com/api/chat.postMessage', headers=myHeaders, data=json.dumps(myPayload))

# CREON Plus 공통 Object 현재 VSCode의 SD1 폴더는 64-bit 가상환경이 설치되어 있다. 32-bit 가상환경은 myProj04 폴더에 설치되어 있다. 
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')  # 시스템 상태 정보
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문 관련 도구

def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system() : admin user -> FAILED')
        return False

    # CreonPlus 연결 상태 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system() : connect to CreonPlus server -> FAILED')
        return False

    # CreonPlus에서의 주문처리를 위한 주문 초기화 작업
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')
        return False

    return True

if __name__ == '__main__':
    if check_creon_system() == True:
        obj = win32com.client.Dispatch("DsCbo1.StockMst")
        obj.SetInputValue(0, 'A005930')
        obj.BlockRequest()
        sec = {}
        sec['현재가'] = obj.GetHeaderValue(11)
        sec['전일대비'] = obj.GetHeaderValue(12)

        dbgout('[삼성전자 = ' + str(sec).replace('{', '').replace('}', ']'))
    else:
        print("This User has NOT an Administrator Authority. Or CreonPlus Server is NOT connected. Or Trade Initialization is NOT completed")
