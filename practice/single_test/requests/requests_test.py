# -*- coding: UTF-8 -*-

import requests
import urllib2
import urllib

url = 'http://www.baidu.com'
URL_get = 'http://localhost:8000/get'

def use_simple_urllib2(url):
    response = urllib2.urlopen(url)
    print '>>>>Response Header'
    print response.info()

    print ''.join([line for line in response.readlines()])


def use_params_urllib2():
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    urllib2.urlopen('?'.join([URL_get, '%s']) % params)

"""requests"""

def get_html(url):
    params = {'param1': 'hello'}
    response = requests.get(url, params=params)



# if __name__ == '__main__':
#     use_simple_urllib2(url)


































