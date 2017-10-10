# -*- coding: UTF-8 -*-


import requests
from bs4 import BeautifulSoup
import sys
import lxml
import random

url = 'http://vchart.yinyuetai.com/vchart/trends?area=ML'

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

# print get_agent()

def get_html(url):
    try:
        r = requests.get(url, timeout=30, headers=get_agent())
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print 'Error'

# print get_html(url)

def get_content(url):

    # 初始化一个列表存储我们需要的信息
    # comments = []

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # print soup

    # 找到所有li标签的条目信息
    LiTargs = soup.find_all('li', class_='vitem J_li_toggle_date ')

    # print LiTargs

    # sys.exit(0)

    # 遍历 li 标签， 拿到我们需要的信息
    for li in LiTargs:
        # 初始化一个字典存储信息
        comment = {}
        # 防止爬虫因找不到信息而停止
        try:
            comment['Top'] = li.find('div', class_='top_num').text.strip().encode('utf-8')
            # print comment
            # sys.exit(0)
            comment['Score'] = li.find('h3', class_='asc_score').text.strip().encode('utf-8')
            comment['MV_name'] = li.find('a', class_='mvname').text.strip().encode('utf-8')
            comment['Time'] = li.find('p', class_='c9').text.strip().encode('utf-8')
            comment['Name'] = li.find('a', class_='special').text.strip().encode('utf-8')
            # comments.append(comment)d

        except:
            print 'Something is Wrong'
            # print comment
            # sys.exit(0)
    # return comments
        print(comment)

# get_content(url)

def main(base_url):

    list = ['ML', 'HT', 'US', 'KR', 'JP']
    url_list = []
    for i in list:
        url = base_url + i
        url_list.append(url)
    # print url_list
    # sys.exit(0)

    for url in url_list:
        if url[-2:] == "ML":
            print("内地排行榜")
        elif url[-2:] == "HT":
            print("香港排行榜")
        elif url[-2:] == "US":
            print("欧美排行榜")
        elif url[-2:] == "KR":
            print("韩国排行榜")
        else:
            print("日本排行榜")
        get_content(url)
        # for comment in comments:d
        #     print comment


base_url = 'http://vchart.yinyuetai.com/vchart/trends?area='


if __name__ == '__main__':
    main(base_url)





























