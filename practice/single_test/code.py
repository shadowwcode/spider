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
    finally:
        print 'End of the file!'


print get_html(url)


if __name__ == '__main__':
    pass







