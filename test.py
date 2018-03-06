#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 10:03
# @Author  : ZQY
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test.html', 'r', encoding='utf-8'), 'lxml')

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