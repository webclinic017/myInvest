import requests
import json

SLACK_BOT_TOKEN = "xoxb-1892258795171-1906429068097-YeoZUcKTm8ZwtantfeCj99Z7"
myHeaders = {
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
    }

myChannel = '#trading'
myText = "TEST : Hi, Very Nice Day !"
myPayload = {
    'channel': myChannel,
    'text': myText
    }
r = requests.post('https://slack.com/api/chat.postMessage', headers=myHeaders, data=json.dumps(myPayload))