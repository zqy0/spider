#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 13:40
# @Author  : ZQY
# @Site    : 
# @File    : clawer_v1.py
# @Software: PyCharm


from bs4 import BeautifulSoup
import requests
import re

default_url = 'http://58.192.29.142/simscxall/Default.aspx'
userRecord_url = 'http://58.192.29.142/simscxall/usedRecord.aspx'

# 创建一个Session会话
session = requests.Session()


# r = session.get(default_url)
# soup = BeautifulSoup(r.content, 'lxml')
# VIEWSTATE = soup.find(id='__VIEWSTATE')['value']


def get_html(drxiaoqu='3', drlouming='55', drceng='3256', drfangjian='850', radio='usedR', txtstart='2018-01-01', txtend='2018-01-18'):

    # VIEWSTATE = '/wEPDwUJLTI5NzY1NzY0D2QWAgIBD2QWCAIBDxBkDxYEZgIBAgICAxYEEAUG5qCh5Yy6ZWcQBQzpgJrngYzmoKHljLoFATFnEAUU6IuN5qKn5qCh5Yy6QUTljLpCMTMFATJnEAUQ6IuN5qKn5qCh5Yy6QuWMugUBM2cWAQICZAIDDxYCHgdWaXNpYmxlZxYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIUk9PTU5BTUUeDkRhdGFWYWx1ZUZpZWxkBQZST09NSUQeC18hRGF0YUJvdW5kZ2QQFRIG5qW85ZCND0HljLowMeWPt+alvCAgIA9B5Yy6MDLlj7fmpbwgICAPQeWMujAz5Y+35qW8ICAgD0HljLowNOWPt+alvCAgIA9B5Yy6MDjlj7fmpbwgICAPQeWMujA55Y+35qW8ICAgD0HljLoxMOWPt+alvCAgIA9C5Yy6MTPlj7fmpbwgICAPROWMujA15Y+35qW8ICAgD0TljLowNuWPt+alvCAgIA9E5Yy6MDnlj7fmpbwgICAPROWMujEw5Y+35qW8ICAgD0TljLowOOWPt+alvCAgIA9E5Yy6MDflj7fmpbwgICAPQeWMujA25Y+35qW8ICAgD0HljLowNeWPt+alvCAgIA9B5Yy6MDflj7fmpbwgICAVEgACNTICNTMCNTQCNTUCNTYCNTcCNTgCNjACNjECNjICNjMCNjQEMjkzNQQyOTM2BDIxOTEEMjE5MgQyMTkzFCsDEmdnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgtkAgUPZBYCAgEPEGQQFQEG5qW85bGCFQEAFCsDAWcWAWZkAgcPFgIfAGcWAgIBDxAPFgYfAQUIUk9PTU5BTUUfAgUGcm9vbWlkHwNnZBAViwEG5oi/6Ze0DEQwOS0xMDEgICAgIAxEMDktMTAyICAgICAMRDA5LTEwMyAgICAgDEQwOS0xMDQgICAgIAxEMDktMTA1ICAgICAMRDA5LTEwNiAgICAgDEQwOS0xMDcgICAgIAxEMDktMTA4ICAgICAMRDA5LTEwOSAgICAgDEQwOS0xMTAgICAgIAxEMDktMTExICAgICAMRDA5LTExMiAgICAgDEQwOS0xMTMgICAgIAxEMDktMTE0ICAgICAMRDA5LTExNSAgICAgDEQwOS0xMTYgICAgIAxEMDktMTE3ICAgICAMRDA5LTExOCAgICAgDEQwOS0xMTkgICAgIAxEMDktMTIwICAgICAMRDA5LTEyMSAgICAgDEQwOS0xMjIgICAgIAxEMDktMjAxICAgICAMRDA5LTIwMiAgICAgDEQwOS0yMDMgICAgIAxEMDktMjA0ICAgICAMRDA5LTIwNSAgICAgDEQwOS0yMDYgICAgIAxEMDktMjA3ICAgICAMRDA5LTIwOCAgICAgDEQwOS0yMDkgICAgIAxEMDktMjEwICAgICAMRDA5LTIxMSAgICAgDEQwOS0yMTIgICAgIAxEMDktMjEzICAgICAMRDA5LTIxNCAgICAgDEQwOS0yMTUgICAgIAxEMDktMjE2ICAgICAMRDA5LTIxNyAgICAgDEQwOS0yMTggICAgIAxEMDktMjE5ICAgICAMRDA5LTIyMCAgICAgDEQwOS0yMjEgICAgIAxEMDktMjIyICAgICAMRDA5LTIyNCAgICAgDEQwOS0zMDEgICAgIAxEMDktMzAyICAgICAMRDA5LTMwMyAgICAgDEQwOS0zMDQgICAgIAxEMDktMzA1ICAgICAMRDA5LTMwNiAgICAgDEQwOS0zMDcgICAgIAxEMDktMzA4ICAgICAMRDA5LTMwOSAgICAgDEQwOS0zMTAgICAgIAxEMDktMzExICAgICAMRDA5LTMxMiAgICAgDEQwOS0zMTMgICAgIAxEMDktMzE0ICAgICAMRDA5LTMxNSAgICAgDEQwOS0zMTYgICAgIAxEMDktMzE3ICAgICAMRDA5LTMxOCAgICAgDEQwOS0zMTkgICAgIAxEMDktMzIwICAgICAMRDA5LTMyMSAgICAgDEQwOS0zMjIgICAgIAxEMDktMzI0ICAgICAMRDA5LTQwMSAgICAgDEQwOS00MDIgICAgIAxEMDktNDAzICAgICAMRDA5LTQwNCAgICAgDEQwOS00MDUgICAgIAxEMDktNDA2ICAgICAMRDA5LTQwNyAgICAgDEQwOS00MDggICAgIAxEMDktNDA5ICAgICAMRDA5LTQxMCAgICAgDEQwOS00MTEgICAgIAxEMDktNDEyICAgICAMRDA5LTQxMyAgICAgDEQwOS00MTQgICAgIAxEMDktNDE1ICAgICAMRDA5LTQxNiAgICAgDEQwOS00MTcgICAgIAxEMDktNDE4ICAgICAMRDA5LTQxOSAgICAgDEQwOS00MjAgICAgIAxEMDktNDIxICAgICAMRDA5LTQyMiAgICAgDEQwOS00MjQgICAgIAxEMDktNTAxICAgICAMRDA5LTUwMiAgICAgDEQwOS01MDMgICAgIAxEMDktNTA0ICAgICAMRDA5LTUwNSAgICAgDEQwOS01MDYgICAgIAxEMDktNTA3ICAgICAMRDA5LTUwOCAgICAgDEQwOS01MDkgICAgIAxEMDktNTEwICAgICAMRDA5LTUxMSAgICAgDEQwOS01MTIgICAgIAxEMDktNTEzICAgICAMRDA5LTUxNCAgICAgDEQwOS01MTUgICAgIAxEMDktNTE2ICAgICAMRDA5LTUxNyAgICAgDEQwOS01MTggICAgIAxEMDktNTE5ICAgICAMRDA5LTUyMCAgICAgDEQwOS01MjEgICAgIAxEMDktNTIyICAgICAMRDA5LTUyNCAgICAgDEQwOS02MDEgICAgIAxEMDktNjAyICAgICAMRDA5LTYwMyAgICAgDEQwOS02MDQgICAgIAxEMDktNjA1ICAgICAMRDA5LTYwNiAgICAgDEQwOS02MDcgICAgIAxEMDktNjA4ICAgICAMRDA5LTYwOSAgICAgDEQwOS02MTAgICAgIAxEMDktNjExICAgICAMRDA5LTYxMiAgICAgDEQwOS02MTMgICAgIAxEMDktNjE0ICAgICAMRDA5LTYxNSAgICAgDEQwOS02MTYgICAgIAxEMDktNjE3ICAgICAMRDA5LTYxOCAgICAgDEQwOS02MTkgICAgIAxEMDktNjIwICAgICAMRDA5LTYyMSAgICAgDEQwOS02MjIgICAgIAxEMDktNjI0ICAgICAQ5LiA5bGC5rW05a6kICAgIBWLAQAEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMgQyMDIzBDIwMjQEMjAyNQQyMDI2BDIwMjcEMjAyOAQyMDI5BDIwMzAEMjAzMQQyMDMyBDIwMzMEMjAzNAQyMDM3BDIwMzgEMjAzOQQyMDQwBDIwNDEEMjA0MgQyMDQzBDIwNDQEMjA0NQQyMDQ2BDIwNDcEMjA0OAQyMDQ5BDIwNTAEMjA1MQQyMDUyBDIwNTMEMjA1NAQyMDU1BDIwNTYEMjA1NwQyMDU4BDIwNjAEMjA2MwQyMDY0BDIwNjUEMjA2NgQyMDY3BDIwNjgEMjA2OQQyMDcwBDIwNzEEMjA3MgQyMDczBDIwNzQEMjA3NQQyMDc2BDIwNzcEMjA3OAQyMDc5BDIwODAEMjA4MQQyMDgyBDIwODMEMjA4NAQyMDg2BDIwOTAEMjA5MQQyMDkyBDIwOTMEMjA5NAQyMDk1BDIwOTYEMjA5NwQyMDk4BDIwOTkEMjEwMAQyMTAxBDIxMDIEMjEwMwQyMTA0BDIxMDUEMjEwNgQyMTA3BDIxMDgEMjEwOQQyMTEwBDIxMTEEMjExMwQyMTE2BDIxMTcEMjExOAQyMTE5BDIxMjAEMjEyMQQyMTIyBDIxMjMEMjEyNAQyMTI2BDIxMjcEMjEyOAQyMTI5BDIxMzAEMjEzMQQyMTMyBDIxMzMEMjEzNAQyMTM1BDIxMzYEMjEzNwQyMTM4BDIxNDAEMjE0MwQyMTQ0BDIxNDUEMjE0NgQyMTQ3BDIxNDgEMjE0OQQyMTUwBDIxNTEEMjE1MgQyMTUzBDIxNTQEMjE1NQQyMTU2BDIxNTcEMjE1OAQyMTU5BDIxNjAEMjE2MQQyMTYyBDIxNjMEMjE2NAQyMTY2BDIxNzUUKwOLAWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUEYnV5UgUFdXNlZFIFDEltYWdlQnV0dG9uMQUMSW1hZ2VCdXR0b24yw6pCyBcZlhCnJok5y9Kf0cba4YeHwXNtcUjLGaH4miw='
    # drxiaoqu = ''
    # drlouming = ''
    # drfangjian = ''
    # radio = ''
    #
    VIEWSTATE = open('viewstate2.txt', 'r', encoding='utf-8')
    ImageButton1x = '43'
    ImageButton1y = '28'

    default_data = {'__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': VIEWSTATE,
                    'drxiaoqu': drxiaoqu,
                    'drlouming': drlouming,
                    'drceng': drceng,
                    'drfangjian': drfangjian,
                    'radio': radio,
                    'ImageButton1.x': ImageButton1x,
                    'ImageButton1.y': ImageButton1y,
                    }
    userRecord_data = {'__VIEWSTATE': '/wEPDwULLTE0ODczMDEwNjlkZBlg1O5faxP/z435MYnGH249r00eW+BbwGL29NzizhTq',
                       '__EVENTVALIDATION': '/wEWBALc36PcDwLE2qDzBgKG+5Y+AouTwe8Che6m/o1/82BbaZcxbpZlxm8QKQMyOdJUvvup/LihY9M=',
                       'txtstart': txtstart,
                       'txtend': txtend,
                       'btnser': '查询',
                       }

    # post传入宿舍号等信息，必须，req是点击登录按钮之后的响应
    req = session.post(default_url, data=default_data)

    # post传入日期参数
    req2 = session.post(userRecord_url, data=userRecord_data)
    # print(req2.text)

    # soup0 = BeautifulSoup(req2.content, 'lxml')
    # current_money = soup0.find('span', class_="number orange").get_text()
    # print(current_money)
    # current_time = soup0.find(class_="status").contents[0].strip()
    # print(current_time)

    # soup = BeautifulSoup(req2.content, 'lxml')
    # # 返回列表迭代器
    # pageer = soup.find(attrs={'class': 'pageControl'}).children
    # # print(pageer)
    # # 找到尾页页数,此实现有问题 考虑如何取出循环里的值
    #
    # for i in pageer:
    #     if i.string == '尾页':
    #         print(i['href'])
    #         global end_pager
    #         end_pager = i['href'].split('=')[-1]

    # 使用正则匹配出尾页数字

    end_pager_href = re.search(u'<a href="usedRecord.aspx\?p=[0-9]+">尾页</a>', req2.text)
    if end_pager_href is not None:
        # print(end_pager_href)
        end_pager_str = end_pager_href.group().split('"')[1]
        # print(type(end_pager_str))
        # print(end_pager_str)
        # 获得尾页数字
        end_pager_num = int(end_pager_str.split('=')[1])
        """
            遍历每页，并提取每页需要的数据
            ----http://58.192.29.142/simscxall/usedRecord.aspx?p=1----
            ----http://58.192.29.142/simscxall/usedRecord.aspx?p=end_pager_num+1----
        """
        with open('a4423.csv', 'a') as f:

            f.write('datetime,used_power,surplus_power\n')
            for page in range(1, end_pager_num+1):
                req3 = session.get(userRecord_url, params={'p': page})
                # print(req3.text)
                soup = BeautifulSoup(req3.content, 'lxml')

                current_money = soup.find('span', class_="number orange").get_text()
                print(current_money)
                current_time = soup.find(class_="status").contents[0].strip()
                print(current_time)

                table = soup.find('table')
                tr_all = table.find_all('tr', class_="contentLine")
                for tr in tr_all:
                    # 日期
                    datetime = tr.find('td').get_text()
                    # 已使用电量
                    used_power = tr.find('td').find_next_sibling('td').get_text()
                    # 剩余电量
                    surplus_power = tr.find('td').find_next_sibling('td').find_next_sibling('td').get_text()
                    print(str(datetime) + ',' + str(used_power) + ',' + str(surplus_power))
                    # 写入文件
                    f.write(str(datetime) + ',' + str(used_power) + ',' + str(surplus_power) + '\n')

    session.close()


if __name__ == '__main__':
    get_html(txtstart='2016-08-25',txtend='2018-01-18')
