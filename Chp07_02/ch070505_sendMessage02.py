import requests
import json

SLACK_BOT_TOKEN = "xoxb-1892258795171-1906429068097-YeoZUcKTm8ZwtantfeCj99Z7"
myHeaders = {
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
    }

myChannel = '#trading'
markdown_text = 'This message is plain.'
myText = "Hello, My Friends !"
myPayload = {
    "channel": myChannel,
    "attachments": [
        {
	        "mrkdwn_in": ["text"],
            "color": "#36a64f",
            "pretext": markdown_text,
            "author_name": "전세용",
            "author_link": "http://flickr.com/bobby/",
            "author_icon": "https://placeimg.com/16/16/people",
            "title": "오늘의 증시 KOSPI",
            "title_link": "https://finance.naver.com/main/main.nhn",
            "text": "코스피 2,996.35  ▽8.39  -0.28%",
            "image_url": 'ssl.pstatic.net/imgstock/chart3/day/KOSPI.png',
            "fields": [
                {
                    "title": "A field's title",
                    "value": "This field's value",
                    "short": False
                },
                {
                    "title": "A short field's title",
                    "value": "A short field's value",
                    "short": True
                },
                {
                    "title": "A second short field's title",
                    "value": "A second short field's value",
                    "short": True
                }
            ],
            "thumb_url": "http://placekitten.com/g/200/200",
            "footer": "footer",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 167856789
        }
    ]
}

r = requests.post('https://slack.com/api/chat.postMessage', headers=myHeaders, data=json.dumps(myPayload))


