import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', charset='utf8')
curs = conn.cursor()

sql = "SELECT * FROM company_info"
df = pd.read_sql(sql, conn)
# for idx in range(len(df)):
for idx in range(2):
    myCode = df['code'].values[idx]
    sql = f"SELECT COUNT(*) FROM daily_price WHERE code={myCode}"
    curs.execute(sql)
    myResult = curs.fetchone()
    print(f"[{idx:04d}] = {myCode},   rows = {myResult[0]}")
    myRows = int(myResult[0])
    print(f'Type of myRows : {type(myRows)}, Value of myRows : {myRows}')

    aa = divmod(myRows, 10)
    print(f'Pages : {aa[0]}, mode : {aa[1]}')

    if aa[1] == 0:
        bb = aa[0]
    else:
        bb = aa[0]+1
    print(f'Total Pages : {bb}')

conn.close()