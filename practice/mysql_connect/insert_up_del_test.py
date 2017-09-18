# -*- coding: UTF-8 -*-

import MySQLdb

conn = MySQLdb.Connect(
    host='10.0.0.112',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8'
)

cursor = conn.cursor()

sql_insert = 'insert into users values(11, \'name11\')'
sql_update = 'update users set user_id = 20 where user_id = 10'
sql_del = 'delete from users where user_id < 3'

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_del)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()







