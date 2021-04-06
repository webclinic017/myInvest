# ch05_03_04_SelectVersion.py

import pymysql

myConn = pymysql.connect(host='localhost', port=3306, db='StockDB', user='root', passwd='2543', charset='utf8', autocommit=True)

'''
myCursor = myConn.cursor()     # Tuple Data Type으로 결과 Return
myCursor.execute("SELECT VERSION();")
result = myCursor.fetchone()

print("Data Type of 'result' : ", type(result))
print("'result' : ", result)
print("'result' : ", result[0])
'''

myCursor = myConn.cursor(pymysql.cursors.DictCursor)   # Dictionary Data Type으로 결과 Return
myCursor.execute("SELECT VERSION();")
result = myCursor.fetchone()

print("Data Type of 'result' : ", type(result))
print("'result' : ", result)
print("'result' : ", result['VERSION()'])

myConn.close()
