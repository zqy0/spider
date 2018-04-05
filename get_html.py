# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Time    : 2018/4/5 10:32
    @Author  : ZQY
    @Email   : 805892567@qq.com
    @Github   : zqy0
    @Software: PyCharm
-------------------------------------------------
    @File    : get_html.py
    @Description :获取房间value值时需要的html内容
-------------------------------------------------
    @Change Activity:
                   2018/4/5 10:32:
-------------------------------------------------
"""

import requests

default_url = 'http://58.192.29.142/simscxall/Default.aspx'


r = requests.get(default_url)
print(r.text)

# VIEWSTATE = open('viewstate3.txt', 'r', encoding='utf-8')
# drxiaoqu = '3'
# drlouming = '51'
# # drfangjian = '2064'
#
#
# default_data = {'__EVENTTARGET': '',
#                 '__EVENTARGUMENT': '',
#                 '__LASTFOCUS': '',
#                 '__VIEWSTATE': VIEWSTATE,
#                 'drxiaoqu': drxiaoqu,
#                 'drlouming': drlouming,
#                 # 'drfangjian': drfangjian,
#                 }
#
# req = requests.post(default_url, data=default_data)
# print(req.text)

