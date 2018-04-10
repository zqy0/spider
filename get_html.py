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
from bs4 import BeautifulSoup
import pandas as pd
# 防止excel打开csv乱码
import codecs
import time
"""
drceng为None时表示获取每幢楼的楼层信息
"""

def get_html(drxiaoqu='3', drlouming='52', drceng='69', VIEWSTATE = open('viewstate3.txt', 'r', encoding='utf-8')):
    default_url = 'http://58.192.29.142/simscxall/Default.aspx'
    # 默认drlouming，drceng VIEWSTATE 不变以便抓取全部vie
    # VIEWSTATE = open('viewstate3.txt', 'r', encoding='utf-8')

    default_data = {'__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': VIEWSTATE,
                    'drxiaoqu': drxiaoqu,
                    'drlouming': drlouming,
                    'drceng': drceng,
                    }
    req = requests.post(default_url, data=default_data)
    # print(req.text)
    return req.text


def drceng_html_to_csv(html):

    soup = BeautifulSoup(html, "lxml")
    vie = soup.find(id='__VIEWSTATE')['value']

    drceng = soup.find(id='drceng')
    options = drceng.find_all('option')

    # 获取当前选中的校区和楼名
    current_selected = soup.find_all('option',attrs={'selected':'selected'})

    info_list = []
    # 消除最后一个的逗号 循化两次故在第二次不加逗号

    for i in current_selected[:2]:
        value = i['value']
        info_list.append(value)
        info_list.append(i.text.strip())
    # print(info_list)

    with codecs.open('G:\python\spider\dict_sheet_v2\dict.csv', 'a+', encoding='utf_8_sig') as f:

        for option in options:
            value = option['value']
            if value != '':
                # print(value + ',' + option.text.strip())
                info = info_list[0] + ',' + info_list[1] + ',' + info_list[2] + ',' + info_list[3] + ','\
                       + value + ',' + option.text.strip() + ',' + vie
                f.write(info+'\n')
            else:
                pass



def fangjian_html_to_csv(html):

    soup = BeautifulSoup(html, "lxml")
    vie = soup.find(id='__VIEWSTATE')['value']

    fangjian = soup.find(id='fangjian')

    options = fangjian.find_all('option')
    # 获取当前选中的校区和楼名和楼层
    current_selected = soup.find_all('option',attrs={'selected':'selected'})

    info_list = []
    for i in current_selected[:3]:
        value = i['value']
        info_list.append(value)
        info_list.append(i.text.strip())
    print(info_list)

    with codecs.open('G:\python\spider\dict_sheet_v2\dict_all.csv', 'a+', encoding='utf_8_sig') as f:
        # f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,fangjian_id,fangjian_info\n')

        for option in options:
            value = option['value']
            if value != '':
                print(value + ',' + option.text.strip())
                f.write(info_list[0]+','+info_list[1]+','+info_list[2]+','+info_list[3]+','+info_list[4]+','+
                        info_list[5]+','+value+','+option.text.strip()+','+vie+'\n')
            else:
                pass

def get_louceng_csv():
    louming = pd.read_csv('G:\Python\spider\dict_sheet\ABD.csv')
    louming_id = louming['louming_id'].tolist()
    print(louming_id)

    with codecs.open('G:\python\spider\dict_sheet_v2\dict.csv', 'w', encoding='utf_8_sig') as f:
        f.write(
            'xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,viewstate\n')
    # drceng_html_to_csv(get_html())

    for i in louming_id:
        html = get_html(drlouming=str(i))
        drceng_html_to_csv(html)

def get_fangjian_csv():
    lou_df = pd.read_csv('G:\Python\spider\dict_sheet_v2\dict.csv')
    louming_id = lou_df['louming_id']
    with codecs.open('G:\python\spider\dict_sheet_v2\dict_all.csv', 'w', encoding='utf_8_sig') as f:
        f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,fangjian_id,fangjian_info,viewstate\n')

    # 选择不了其他楼层的原因是每幢楼VIE不同
    # html = get_html(drlouming='52', drceng='69')
    # print(html)
    # fangjian_html_to_csv(get_html(drlouming='52',drceng='69'))

    for i in set(louming_id):

        for j in lou_df[lou_df['louming_id'].values == i]['louceng_id']:
            print(i, j)
            vie = lou_df[lou_df['louceng_id'].values==j]['viewstate']
            html = get_html(drlouming=str(i),drceng=str(j),VIEWSTATE=vie)
            fangjian_html_to_csv(html)

if __name__ == '__main__':
    get_fangjian_csv()
    # get_louceng_csv()
