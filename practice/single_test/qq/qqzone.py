# -*- coding: UTF-8 -*-

import practice.single_test.requests
import sys
from bs4 import BeautifulSoup
import lxml
import random


url = 'https://user.qzone.qq.com/295329847/infocenter?via=toolbar&_t_=0.6737937242204142'

def get_agent():
    """
    模拟 header 的 user-agent 字段
    返回一个随机的 user-agent 字典类型的键值对
    """
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader

def get_html(url):
    try:
        r = practice.single_test.requests.get(url, timeout=30, headers=get_agent())
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print 'Error'
    return r.text


if __name__ == '__main__':
    print get_html(url)






















