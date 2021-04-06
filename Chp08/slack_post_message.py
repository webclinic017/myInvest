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

dbgout('[삼성전자 : 81,500, 전일대비 : +300]')