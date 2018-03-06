#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 8:46
# @Author  : ZQY
# @Site    : 
# @File    : transform_name.py
# @Software: PyCharm

"""
URL：http://58.192.29.142/simscxall/Default.aspx
将楼名房间名转化为相应的value值
<option value="1220">A10-102     </option>
"""
import requests
from bs4 import BeautifulSoup

default_url = 'http://58.192.29.142/simscxall/Default.aspx'

# VIEWSTATE = open('viewstate.txt', 'r', encoding='utf-8')
VIEWSTATE = '/wEPDwUJLTI5NzY1NzY0D2QWAgIBD2QWCAIBDxBkDxYEZgIBAgICAxYEEAUG5qCh5Yy6ZWcQBQzpgJrngYzmoKHljLoFATFnEAUU6IuN5qKn5qCh5Yy6QUTljLpCMTMFATJnEAUQ6IuN5qKn5qCh5Yy6QuWMugUBM2cWAQICZAIDDxYCHgdWaXNpYmxlZxYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIUk9PTU5BTUUeDkRhdGFWYWx1ZUZpZWxkBQZST09NSUQeC18hRGF0YUJvdW5kZ2QQFRIG5qW85ZCND0HljLowMeWPt+alvCAgIA9B5Yy6MDLlj7fmpbwgICAPQeWMujAz5Y+35qW8ICAgD0HljLowNOWPt+alvCAgIA9B5Yy6MDjlj7fmpbwgICAPQeWMujA55Y+35qW8ICAgD0HljLoxMOWPt+alvCAgIA9C5Yy6MTPlj7fmpbwgICAPROWMujA15Y+35qW8ICAgD0TljLowNuWPt+alvCAgIA9E5Yy6MDnlj7fmpbwgICAPROWMujEw5Y+35qW8ICAgD0TljLowOOWPt+alvCAgIA9E5Yy6MDflj7fmpbwgICAPQeWMujA25Y+35qW8ICAgD0HljLowNeWPt+alvCAgIA9B5Yy6MDflj7fmpbwgICAVEgACNTICNTMCNTQCNTUCNTYCNTcCNTgCNjACNjECNjICNjMCNjQEMjkzNQQyOTM2BDIxOTEEMjE5MgQyMTkzFCsDEmdnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgtkAgUPZBYCAgEPEGQQFQEG5qW85bGCFQEAFCsDAWcWAWZkAgcPFgIfAGcWAgIBDxAPFgYfAQUIUk9PTU5BTUUfAgUGcm9vbWlkHwNnZBAViwEG5oi/6Ze0DEQwOS0xMDEgICAgIAxEMDktMTAyICAgICAMRDA5LTEwMyAgICAgDEQwOS0xMDQgICAgIAxEMDktMTA1ICAgICAMRDA5LTEwNiAgICAgDEQwOS0xMDcgICAgIAxEMDktMTA4ICAgICAMRDA5LTEwOSAgICAgDEQwOS0xMTAgICAgIAxEMDktMTExICAgICAMRDA5LTExMiAgICAgDEQwOS0xMTMgICAgIAxEMDktMTE0ICAgICAMRDA5LTExNSAgICAgDEQwOS0xMTYgICAgIAxEMDktMTE3ICAgICAMRDA5LTExOCAgICAgDEQwOS0xMTkgICAgIAxEMDktMTIwICAgICAMRDA5LTEyMSAgICAgDEQwOS0xMjIgICAgIAxEMDktMjAxICAgICAMRDA5LTIwMiAgICAgDEQwOS0yMDMgICAgIAxEMDktMjA0ICAgICAMRDA5LTIwNSAgICAgDEQwOS0yMDYgICAgIAxEMDktMjA3ICAgICAMRDA5LTIwOCAgICAgDEQwOS0yMDkgICAgIAxEMDktMjEwICAgICAMRDA5LTIxMSAgICAgDEQwOS0yMTIgICAgIAxEMDktMjEzICAgICAMRDA5LTIxNCAgICAgDEQwOS0yMTUgICAgIAxEMDktMjE2ICAgICAMRDA5LTIxNyAgICAgDEQwOS0yMTggICAgIAxEMDktMjE5ICAgICAMRDA5LTIyMCAgICAgDEQwOS0yMjEgICAgIAxEMDktMjIyICAgICAMRDA5LTIyNCAgICAgDEQwOS0zMDEgICAgIAxEMDktMzAyICAgICAMRDA5LTMwMyAgICAgDEQwOS0zMDQgICAgIAxEMDktMzA1ICAgICAMRDA5LTMwNiAgICAgDEQwOS0zMDcgICAgIAxEMDktMzA4ICAgICAMRDA5LTMwOSAgICAgDEQwOS0zMTAgICAgIAxEMDktMzExICAgICAMRDA5LTMxMiAgICAgDEQwOS0zMTMgICAgIAxEMDktMzE0ICAgICAMRDA5LTMxNSAgICAgDEQwOS0zMTYgICAgIAxEMDktMzE3ICAgICAMRDA5LTMxOCAgICAgDEQwOS0zMTkgICAgIAxEMDktMzIwICAgICAMRDA5LTMyMSAgICAgDEQwOS0zMjIgICAgIAxEMDktMzI0ICAgICAMRDA5LTQwMSAgICAgDEQwOS00MDIgICAgIAxEMDktNDAzICAgICAMRDA5LTQwNCAgICAgDEQwOS00MDUgICAgIAxEMDktNDA2ICAgICAMRDA5LTQwNyAgICAgDEQwOS00MDggICAgIAxEMDktNDA5ICAgICAMRDA5LTQxMCAgICAgDEQwOS00MTEgICAgIAxEMDktNDEyICAgICAMRDA5LTQxMyAgICAgDEQwOS00MTQgICAgIAxEMDktNDE1ICAgICAMRDA5LTQxNiAgICAgDEQwOS00MTcgICAgIAxEMDktNDE4ICAgICAMRDA5LTQxOSAgICAgDEQwOS00MjAgICAgIAxEMDktNDIxICAgICAMRDA5LTQyMiAgICAgDEQwOS00MjQgICAgIAxEMDktNTAxICAgICAMRDA5LTUwMiAgICAgDEQwOS01MDMgICAgIAxEMDktNTA0ICAgICAMRDA5LTUwNSAgICAgDEQwOS01MDYgICAgIAxEMDktNTA3ICAgICAMRDA5LTUwOCAgICAgDEQwOS01MDkgICAgIAxEMDktNTEwICAgICAMRDA5LTUxMSAgICAgDEQwOS01MTIgICAgIAxEMDktNTEzICAgICAMRDA5LTUxNCAgICAgDEQwOS01MTUgICAgIAxEMDktNTE2ICAgICAMRDA5LTUxNyAgICAgDEQwOS01MTggICAgIAxEMDktNTE5ICAgICAMRDA5LTUyMCAgICAgDEQwOS01MjEgICAgIAxEMDktNTIyICAgICAMRDA5LTUyNCAgICAgDEQwOS02MDEgICAgIAxEMDktNjAyICAgICAMRDA5LTYwMyAgICAgDEQwOS02MDQgICAgIAxEMDktNjA1ICAgICAMRDA5LTYwNiAgICAgDEQwOS02MDcgICAgIAxEMDktNjA4ICAgICAMRDA5LTYwOSAgICAgDEQwOS02MTAgICAgIAxEMDktNjExICAgICAMRDA5LTYxMiAgICAgDEQwOS02MTMgICAgIAxEMDktNjE0ICAgICAMRDA5LTYxNSAgICAgDEQwOS02MTYgICAgIAxEMDktNjE3ICAgICAMRDA5LTYxOCAgICAgDEQwOS02MTkgICAgIAxEMDktNjIwICAgICAMRDA5LTYyMSAgICAgDEQwOS02MjIgICAgIAxEMDktNjI0ICAgICAQ5LiA5bGC5rW05a6kICAgIBWLAQAEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMgQyMDIzBDIwMjQEMjAyNQQyMDI2BDIwMjcEMjAyOAQyMDI5BDIwMzAEMjAzMQQyMDMyBDIwMzMEMjAzNAQyMDM3BDIwMzgEMjAzOQQyMDQwBDIwNDEEMjA0MgQyMDQzBDIwNDQEMjA0NQQyMDQ2BDIwNDcEMjA0OAQyMDQ5BDIwNTAEMjA1MQQyMDUyBDIwNTMEMjA1NAQyMDU1BDIwNTYEMjA1NwQyMDU4BDIwNjAEMjA2MwQyMDY0BDIwNjUEMjA2NgQyMDY3BDIwNjgEMjA2OQQyMDcwBDIwNzEEMjA3MgQyMDczBDIwNzQEMjA3NQQyMDc2BDIwNzcEMjA3OAQyMDc5BDIwODAEMjA4MQQyMDgyBDIwODMEMjA4NAQyMDg2BDIwOTAEMjA5MQQyMDkyBDIwOTMEMjA5NAQyMDk1BDIwOTYEMjA5NwQyMDk4BDIwOTkEMjEwMAQyMTAxBDIxMDIEMjEwMwQyMTA0BDIxMDUEMjEwNgQyMTA3BDIxMDgEMjEwOQQyMTEwBDIxMTEEMjExMwQyMTE2BDIxMTcEMjExOAQyMTE5BDIxMjAEMjEyMQQyMTIyBDIxMjMEMjEyNAQyMTI2BDIxMjcEMjEyOAQyMTI5BDIxMzAEMjEzMQQyMTMyBDIxMzMEMjEzNAQyMTM1BDIxMzYEMjEzNwQyMTM4BDIxNDAEMjE0MwQyMTQ0BDIxNDUEMjE0NgQyMTQ3BDIxNDgEMjE0OQQyMTUwBDIxNTEEMjE1MgQyMTUzBDIxNTQEMjE1NQQyMTU2BDIxNTcEMjE1OAQyMTU5BDIxNjAEMjE2MQQyMTYyBDIxNjMEMjE2NAQyMTY2BDIxNzUUKwOLAWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUEYnV5UgUFdXNlZFIFDEltYWdlQnV0dG9uMQUMSW1hZ2VCdXR0b24yw6pCyBcZlhCnJok5y9Kf0cba4YeHwXNtcUjLGaH4miw='
drxiaoqu = '2'

default_data = {'__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VIEWSTATE': VIEWSTATE,
                'drxiaoqu': drxiaoqu,
                'drlouming': '',
                }



req = requests.post(default_url, data=default_data)

soup = BeautifulSoup(req.content, 'lxml')
print(soup)
louming = soup.find(id='louming')

for i in louming.find_all('option'):
    # 将第一行头信息补全
    if i['value'] == '':
        i['value'] = 'ID'

    print(i['value'] + ',' + i.string.strip())
req.close()

default_data.update({'drlouming': '58'})


req2 = requests.post(default_url, data=default_data)
print(req2)
soup2 = BeautifulSoup(req2.content, 'lxml')
print(soup2)
fangjian = soup2.find(id='fangjian')
print(fangjian)
