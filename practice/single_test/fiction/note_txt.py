# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import codecs
import sys

# url = 'http://www.ty2016.net/net/tctd01/37900.html'

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        print 'error'


# html = get_html(url)
#
# soup = BeautifulSoup(html, 'lxml')
#
# print soup.find('h1').text
# print soup.find('div', attrs={'id': 'main'}).find_all('p')[1].text




def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    comment = {}
    try:
        comment['title'] = soup.find('h1').text
        comment['comment'] = soup.find('div', attrs={'id': 'main'}).find_all('p')[1].text.strip()
        comments.append(comment)
    except:
        print 'Error'

    return comments


def Out2Txt(dict):
    with codecs.open('note.txt', 'a+', 'utf-8') as f:
        for comment in dict:
            f.write(comment['title'] + '\n')
            f.write(comment['comment'] + '\n\n')


    print 'Finshed'



def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + str(37900 + i) + '.html')

    # print url_list

    # sys.exit(0)

    for url in url_list:
        content = get_content(url)
        Out2Txt(content)
    print 'Save done'


base_url = 'http://www.ty2016.net/net/tctd01/'

deep = 20

if __name__ == '__main__':
    pass






