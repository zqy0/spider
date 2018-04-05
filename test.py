#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 10:03
# @Author  : ZQY
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test.html', 'r', encoding='utf-8'), 'lxml')
