#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-03 15:03:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from bs4 import BeautifulSoup
html = open('test1.html', 'r', encoding='utf-8')

soup = BeautifulSoup(html, "lxml")
fangjian = soup.find(id='fangjian')
options = fangjian.find_all('option')

# 获取当前选中的校区和楼名和楼层
current_selected = soup.find_all('option',attrs={'selected':'selected'})

# drxiaoqu,drlouming,drlouceng
with open('I:\python\spider\dict_sheet\dict_1.csv', 'w', encoding='utf-8') as f:
    f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info\n')
    info_list = []
    for i in current_selected[:3]:
        value = i['value']
        f.write(value+','+i.text.strip()+',')
        info_list.append(value)
        info_list.append(i.text.strip())
    print(info_list)

with open('I:\python\spider\dict_sheet\dict.csv', 'w', encoding='utf-8') as f:
    f.write('xiaoqu_id,xiaoqu_info,louming_id,louming_info,louceng_id,louceng_info,fangjian_value,fangjian_info\n')

    for option in options:
        value = option['value']
        if value != '':
            print(value + ',' + option.text.strip())
            f.write(info_list[0]+','+info_list[1]+','+info_list[2]+','+info_list[3]+','+info_list[4]+','+
                    info_list[5]+','+value+','+option.text.strip()+'\n')
        else:
            print('---' + option.text.strip())
