# -*- coding: UTF-8 -*-

import urllib2

url = 'https://en.wikipedia.org/robots.txt'

response = urllib2.urlopen(url)

buf = response.read().decode('utf-8')

print buf





