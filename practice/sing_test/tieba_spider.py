# -*- coding: UTF-8 -*-
# 爬取百度贴吧
# 找到每一篇帖子的 标题、发帖人、日期、楼层、以及跳转链接
# 将结果保存到文本

# 第一页
# url = 'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F%E7%AC%AC%E4%B8%83%E5%AD%A3&ie=utf-8&pn=0'
# 第二页
# url = 'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F%E7%AC%AC%E4%B8%83%E5%AD%A3&ie=utf-8&pn=50'
# 第三页
# url = 'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F%E7%AC%AC%E4%B8%83%E5%AD%A3&ie=utf-8&pn=100'
# 发现页数就是 pn = 50 * (n-1) 便于我们拼接 url

# 通过分析每个帖子都包含在一个  <li class=" j_thread_list clearfix">中
# 帖子链接标题 <a href="/p/5328874747" title="权利的游戏1-7完整版！！！" target="_blank" class="j_th_tit ">权利的游戏1-7完整版！！！</a>
# 作者 <span class="tb_icon_author no_icon_author" title="主题作者: ☞慧💖慧☜" data-field="{"user_id":2551342822}">
# 回帖数量 <div class="col2_left j_threadlist_li_left">
# <span class="threadlist_rep_num center_text" title="回复">19</span>
# </div>
# 时间: <span class="pull-right is_show_create_time" title="创建时间">9-18</span>



import requests
from bs4 import BeautifulSoup
import time
import sys
import MySQLdb


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 我们已经知道百度贴吧的 编码是 utf8 手动设置
        r.encoding = 'utf8'
        return r.text
    except:
        return 'Error'


def get_content(url):
    """分析网页文件，整理信息， 保存在列表变量中"""
    # 初始化一个列表来保存所有帖子的信息
    comments = []
    # 获取源文件
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # 找到所有帖子 li 标签
    liTags =soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # 遍历找到我们需要的信息
    for li in liTags:
        # 初始化一个字典来存储文本信息
        comment = {}
        # 防止爬虫找不到信息而停止
        try:
            comment['title'] = li.find('a', attrs={'class': 'j_th_tit '}).text.strip()
            comment['link'] = 'http://tieba.baidu.com/' + \
                li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find('span', attrs={'class': 'tb_icon_author no_icon_author'}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('something is wrong')
    return comments


def Out2File(dict):
    # """保存到当前目录的 TTbt.txt 文件中"""
    # with open('TTbt.txt', 'a+') as f:
    #     for comment in dict:
    #         f.write('Title: {} \t Link: {} \t Author: {} \t Time: {} \t ReplyNum: {} \t'.format(
    #             comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']
    #         ))
    print('当前页面爬取完成')


class SaveText(object):
    def __init__(self, conn):
        self.conn = conn

    def Save2mysql(self, dict):
        """保存到数据库"""
        cursor = self.conn.cursor()
        for comment in dict:
            print(comment['title'], comment['name'], comment['time'], comment['link'], comment['replyNum'])
            try:
                sql = 'insert into posts(title, author, time, link, reply) values(%s, %s, %s, %s, %s)' % \
                      (comment['title'], comment['name'], comment['time'], comment['link'], comment['replyNum'])
                cursor.execute(sql)
                print('saving')
                rs = cursor.fetchall()
                if len(rs) != 1:
                    raise Exception('error')
            finally:
                cursor.close()


def main(base_url, deep):
    url_list = []
    # 将所有需要爬取的 url 存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有网页已下载到本地, 开始筛选信息')

    conn = MySQLdb.Connect(
        host='10.0.0.112',
        port=3306,
        user='root',
        passwd='123456',
        db='spider',
        charset='utf8'
    )

    tr_save = SaveText(conn)


    # 循环写入数据
    for url in url_list:
        content = get_content(url)
        # print content
        tr_save.Save2mysql(content)
    print('所有信息保存完毕')

base_url = 'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F%E7%AC%AC%E4%B8%83%E5%AD%A3&ie=utf-8&pn=0'

deep = 3

if __name__ == '__main__':
    main(base_url, deep)




