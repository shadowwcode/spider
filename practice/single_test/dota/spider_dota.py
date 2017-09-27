# -*- coding: UTF-8 -*-

# 分析得出每个比赛的内容存储在:
# <div class="matchmain bisai_qukuai"> 中

import requests
from bs4 import BeautifulSoup
import lxml
import sys


def get_hitml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print 'Error'


def print_result(url):
    """查询比赛结果， 并格式化输出"""
    html = get_hitml(url)
    soup = BeautifulSoup(html, 'lxml')
    match_list = soup.find_all('div', attrs={'class': 'matchmain bisai_qukuai'})
    for match in match_list:
        time = match.find('div', attrs={'class': 'whenm'}).text.strip()
        team_name = match.find_all('span', attrs={'class': 'team_name'})
        # print team_name[1].string
        # sys.exit(0)


        if team_name[0].string[0:3] == 'php':
            team1_name = 'NoTeam'
        else:
            team1_name = team_name[0].string

        """采用css选择器, 比原来的属性选择更加方便"""
        team1_support_level = match.find('span', class_='team_number_green').string
        # print team1_support_level
        # sys.exit(0)

        team2_name = team_name[1].string
        team2_support_level = match.find('span', class_='team_number_red').string

        print('Time: {}, \n Team1: {} Supporter: {} \n Team2: {} Supporter: {} \n'.\
              format(time, team1_name, team1_support_level, team2_name, team2_support_level))


def main():
    url = 'http://dota2bocai.com/match'
    print_result(url)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    main()





