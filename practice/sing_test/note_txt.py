# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://www.ty2016.net/net/tctd01/37900.html'

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.endcodding = 'gbk'
        return r.text
    except:
        print 'error'

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

html = get_html(url)

soup = BeautifulSoup(html, 'lxml')


# print soup.find('h1').text














