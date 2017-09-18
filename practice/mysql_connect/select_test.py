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

sql = 'select * from users'
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print "userid=%s, username=%s" % row

cursor.close()
conn.close()




