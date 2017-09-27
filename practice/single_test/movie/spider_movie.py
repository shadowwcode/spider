# -*- coding: UTF-8 -*-

# 爬取电影信息 http://dianying.2345.com/top/

# 分析: 电影列表 <ul class="picList clearfix">   名称: <span class="sTit">
# 时间 <span class="sIntro">上映时间：2017-08-03</span>
# 演员: <p class="pActor">
# 简介<p class="pTxt pIntroShow">


import sys
import requests
from bs4 import BeautifulSoup
import lxml
import MySQLdb


class Savetext(object):
    def __init__(self, conn):
        self.conn = conn

    def Save2Database(self, name, time, actor, intro):
        cursor = self.conn.cursor()
        try:
            sql = ('insert into movies values({}, {}, {}, {})'.format(name, time, actor, intro))
            print sql
            cursor.execute(sql)
            print 'saving'
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('error')
        finally:
            cursor.close()


def get_hml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # print r.encoding
        # print r.apparent_encoding
        # r.encoding = r.apparent_encoding
        r.encoding = 'gbk'
        return r.text
    except:
        print 'Error'


def get_content(url):
    html = get_hml(url)
    soup = BeautifulSoup(html, 'lxml')

    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')

    conn = MySQLdb.Connect(
        host='10.0.0.112',
        port=3306,
        user='root',
        passwd='123456',
        db='spider',
        charset='utf8'
    )

    tr_save = Savetext(conn)

    for top in movies:
        image_url = top.find('img')['src']

        name = top.find('span', class_='sTit').text
        try:
            time = top.find('span', class_='sIntro').text
        except:
            print 'None'

        # 这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
        actors = top.find('p', class_='pActor')
        actor = ''
        for act in actors.contents:
            actor = actor + act.string + '  '

        intro = top.find('p', class_='pTxt pIntroShow').text

        # print image_url, name, time, actor, intro
        # sys.exit(0)

        print("Name: {}\t{}\n{}\n{} \n \n".format(name, time, actor, intro))
        tr_save.Save2Database(name, time, actor, intro)


        # 保存图片 出现了一点问题 url 无法打开
        # with open('C:\Users\Administrator\Desktop\movie'+name+'.png', 'wb+') as f:
        #     f.write(requests.get(image_url).content)


def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")



    main()











