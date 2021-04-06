import pandas as pd

df = pd.read_html("https://kind.krx.co.kr/corpgeneral/corpList.do?method=download", header=0)[0]

df['종목코드'] = df['종목코드'].map('{:06d}'.format)
df = df.sort_values(by='종목코드', ascending=True)   # ascending=True : 오름차순 정렬
print(df)
