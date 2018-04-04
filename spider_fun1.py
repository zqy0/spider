#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-03 15:03:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from bs4 import BeautifulSoup
html = open('test.html', 'r', encoding='utf-8')

soup = BeautifulSoup(html, "lxml")
print(soup)

options = soup.find_all('option')

# for i in options:
# 	print(i)

for option in options:
	value = option['value']
	if value != '':
		print(value + ',' + option.text.strip())
		# print(option.text.strip())
	else:
		print('---' + option.text.strip())
