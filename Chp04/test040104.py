import pandas as pd

df = pd.read_excel("C:/Users/cross/Downloads/상장법인목록.xlsx")
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
df = df.sort_values(by='종목코드', ascending=True)   # ascending=True : 오름차순 정렬
print(df)
