# -*- coding: UTF-8 -*-


import re
import requests
import pprint
import sys

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9028'
response = requests.get(url, verify=False)
# print(len(response.text))
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
buffer = pprint.pprint(dict(stations), indent=4)





