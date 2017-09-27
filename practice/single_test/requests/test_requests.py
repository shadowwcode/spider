# -*- coding: UTF-8 -*-

import requests

# hd = {'User-Agent': 'Mozilla/5.0'}
# buf = requests.get('http://www.baidu.com', headers=hd)
#
# print (buf.status_code)
# print (buf.headers)
# print (buf.encoding)
# print (buf.apparent_encoding)
# print (buf.content)

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态吗不为200， 则应发HTTPError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

url = 'http://www.baidu.com'

r = getHtmlText(url)
print len(r)