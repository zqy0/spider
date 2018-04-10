#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8
# @Author  : ZQY
# @Site    :
# @File    : clawer_v2.py
# @Software: PyCharm


from bs4 import BeautifulSoup
import requests
import re
import datetime

default_url = 'http://58.192.29.142/simscxall/Default.aspx'
userRecord_url = 'http://58.192.29.142/simscxall/usedRecord.aspx'

# 创建一个Session会话
session = requests.Session()


# r = session.get(default_url)
# soup = BeautifulSoup(r.content, 'lxml')
# VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
today_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

def get_html(drxiaoqu='3', drlouming='51', drceng='235', drfangjian='285',
             radio='usedR', txtstart='2014-01-01', txtend=today_datetime,file_name='unkown',
             VIEWSTATE= open('viewstate3.txt', 'r', encoding='utf-8')):

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

        with open(file_name+'.csv', 'a+') as f:

            # f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,'
            #         'fangjian_value,fangjian_info,datetimes,used_power,surplus_power\n')
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
                    datetimes = tr.find('td').get_text()
                    # 已使用电量
                    used_power = tr.find('td').find_next_sibling('td').get_text()
                    # 剩余电量
                    surplus_power = tr.find('td').find_next_sibling('td').find_next_sibling('td').get_text()
                    print(drxiaoqu + ',' + drlouming + ',' + drceng + ',' + drfangjian + ',' + str(datetimes) + ',' + str(used_power) + ',' + str(surplus_power))
                    # 写入文件
                    f.write(drxiaoqu + ',' + drlouming + ',' + drceng + ',' + drfangjian + ','
                            +str(datetimes) + ',' + str(used_power) + ',' + str(surplus_power) + '\n')

    session.close()


if __name__ == '__main__':

    # get_html(drxiaoqu='3', drlouming='51', drceng='235', drfangjian='285',file_name='b1-220')

    import pandas as pd

    # with open('data.csv', 'w') as f:
    #
    #     f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,'
    #             'fangjian_value,fangjian_info,datetimes,used_power,surplus_power\n')

    lou_df = pd.read_csv('G:\Python\spider\dict_sheet_v2\dict_all.csv')[388:]
    louming_id = lou_df['louming_id']

    for i in set(louming_id):
        louceng_id = lou_df[lou_df['louming_id'].values == i]['louceng_id']
        for j in set(louceng_id):
            fangjian_id = lou_df[lou_df['louceng_id'].values == j]['fangjian_id']
            for m in fangjian_id:
                print(i, j, m) #_# 3794条 prefect
                vie = lou_df[lou_df['fangjian_id'].values==m]['viewstate']
                get_html(drxiaoqu='3', drlouming=str(i), drceng=str(j), drfangjian=str(m),file_name='data',VIEWSTATE=vie)