import pandas as pd

krx_list = pd.read_html("C:/Users/cross/Downloads/상장법인목록.xls", header=0)

print(krx_list[0])
