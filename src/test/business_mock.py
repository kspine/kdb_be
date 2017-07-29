from __future__ import print_function
import random
import pyodbc

conn = pyodbc.connect('DRIVER=oradriver;DBQ=172.16.1.199:1521/orcl;UID=kylin;PWD=oracle')
cur = conn.cursor()

_id = 1
text = 'ABCDEFGHIJKLMN'
_len = len(text)

try:
    while True:
        _cnt = text[random.randint(0, _len-1)]
        sql = "insert into test values ({0}, '{1}')".format(_id, _cnt)
        print(sql)
        #sql = 'drop table {0}'.format(tab)
        cur.execute(sql)
        cur.commit()
        _id += 1
        import time
        time.sleep(0.1)
except Exception as e:
    print('+++', e)

