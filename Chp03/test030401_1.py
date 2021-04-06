import pandas as pd

'''
# KRX 엑셀파일 다운로드 받아서 종목코드 설정
df_krx = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
# df = pd.read_excel("D:\\sda1\\test01.xlsx", header=0)
df_krx = df_krx.sort_values(['종목코드'], ascending=[True])
df_krx = df_krx[['회사명', '종목코드']]
df_krx = df_krx.rename(columns={'회사명': 'Name', '종목코드': 'Symbol'})
df = df_krx.set_index('Symbol')
df.to_excel("KRX_Symbol01.xlsx")
'''

import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')
df_krx = df_krx.sort_values(['Symbol'], ascending=[True])
df_krx = df_krx[['Name', 'Symbol']]
df = df_krx.set_index('Symbol')
df.to_excel("KRX_Symbol02.xlsx")
