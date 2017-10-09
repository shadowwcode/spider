# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://www.quanshuwang.com'

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print 'Error'

print get_html(url)












