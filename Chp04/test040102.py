import pandas as pd

krx_list = pd.read_html("C:/Users/cross/Downloads/상장법인목록.xls", header=0)

print("\n변경전 종목코드\n", krx_list[0]['종목코드'])
krx_list[0]['종목코드'] = krx_list[0]['종목코드'].map('{:06d}'.format)
print("\n변경후 종목코드\n", krx_list[0]['종목코드'])
