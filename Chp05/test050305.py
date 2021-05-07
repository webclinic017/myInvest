# ch05_03_05_read_krx_code.py

import pymysql

conn = pymysql.connect(host='localhost', port=3306, db='stockdb', user='root', passwd='2543', autocommit=True)



conn.close()

