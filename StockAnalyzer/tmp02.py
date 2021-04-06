import pandas as pd

url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
krx = pd.read_html(url, header=0)[0]
krx = krx[['종목코드', '회사명']]
krx = krx.rename(columns={'종목코드' : 'code', '회사명' : 'company'})
krx.code = krx.code.map('{:06d}'.format)

print(krx)