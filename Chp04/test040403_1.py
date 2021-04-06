# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

'''
네이버 증권사이트(일별 시세)에서 모든 페이지 정보 가져오기
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup

# __author__ = 'Wonjin Kim <devopia@naver.com>'

# 네이버 금융 주식 일별 시세 URL
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

# 해당 사이트는 반드시 헤더 정보를 요구하기 때문에 헤더를 넘겨줘야 함
headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
req = requests.get(url, headers = headers)

# 첫 페이지를 파싱하여 전체 페이지 수 계산
soup = BeautifulSoup(req.text, 'html.parser')
last_page = int(soup.select_one('td.pgRR').a['href'].split('=')[-1])

# 모든 페이지 정보 데이터 프레임 생성
df = None
for page in range(1, last_page + 1):
    req = requests.get(f'{url}&page={page}', headers = headers)
    df = pd.concat([df, pd.read_html(req.text, encoding = 'euc-kr')[0]], ignore_index = True)

# 데이터가 없는 행 일괄 삭제
df.dropna(inplace = True)

# 인덱스 재 배열
df.reset_index(drop = True, inplace = True)