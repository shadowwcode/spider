# -*- coding: UTF-8 -*-


import urllib2
from bs4 import BeautifulSoup
import re
import MySQLdb

url = 'https://baike.baidu.com/item/%E8%B7%AF%E9%81%A5/216'

request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(request)

buf = response.read()

soup = BeautifulSoup(buf, 'html.parser', from_encoding='utf-8')

full_urls = []
links = soup.find_all('a', href=re.compile(r'/item/(.*)'))
for link in links:
    full_url = 'https://baike.baidu.com' + link['href']
    full_urls.append(full_url)
    # print link.name, link['href'], link.get_text()

    conn = MySQLdb.Connect(
        host='10.0.0.112',
        port=3306,
        user='root',
        passwd='123456',
        db='spider',
        charset='utf8'
    )
    try:
        cursor = conn.cursor()
        sql = 'insert into baike_url(name, url) values (%s, %s)'
        cursor.execute(sql, (link.get_text(), full_url))
        conn.commit()
    finally:
        conn.close()
        cursor.close()

