#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 10:03
# @Author  : ZQY
# @Site    : 
# @File    : b2.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests

def get_html(drxiaoqu = '3', drlouming = '62', drceng = '484',drfangjian='',EVENTTARGET=None):
    default_url = 'http://58.192.29.142/simscxall/Default.aspx'

    f = open('VIE.txt', 'r', encoding='utf-8')
    VIEWSTATE = f.readlines()

    default_data = {'__EVENTTARGET': EVENTTARGET,
                    '__EVENTARGUMENT': VIEWSTATE,
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': '',
                    'drxiaoqu': drxiaoqu,
                    'drlouming': drlouming,
                    'drceng': drceng,
                    'drfangjian': drfangjian,
                    }
    req = requests.post(default_url, data=default_data)

    soup = BeautifulSoup(req.text, "lxml")
    vie = soup.find(id='__VIEWSTATE')
    print(vie['value'])

    # print(req.text)
    return req.text

if __name__ == '__main__':
    print(get_html(EVENTTARGET='drceng'))
