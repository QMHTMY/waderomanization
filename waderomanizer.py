#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Author: Shieber
#    Date: 2019.07.22
#    Modified: 2020.07.24
#
#    1.一键生成中文名威妥玛拼音表示 
#    2.查找中国城市等地区的威妥玛表示
#

import json
from pypinyin import lazy_pinyin 

def character2pinyin(name):
    #获取中文名拼音表示
    py = lazy_pinyin(name) 
    length = len(py)

    with open('pinyin.json','r') as jobj:
        #拼音表
        data = json.load(jobj)
        
        #名字有4,3,2,1个字共四种情况，逐字处理并拼接
        nameparts = None
        if 4 == length:
            nameparts = [data[py[0]], data[py[1]], data[py[2]], data[py[3]] ]
        elif 3 == length:
            nameparts = [data[py[0]], data[py[1]], data[py[2]] ]
        elif 2 == length:
            nameparts = [data[py[0]], data[py[1]] ]
        elif 1 == length:
            fullnm  = data[py[0]].capitalize()
        else:
            fullnm  = '名字长度不正确'

        if nameparts != None:
            fullnm  = ' '.join(nameparts).capitalize() #首字母大写

    print(fullnm)

def districtSearcher(area):
    '''中国地名的威式拼音搜寻器'''
    if '0' == area:
        with open('area.json','r') as jobj:
            areaname = json.load(jobj)
            for k,v in areaname.items():
                print(k,v)
    else:
        with open('area.json','r') as jobj:
            areaname = json.load(jobj)
            try:
                print(areaname[area])
            except KeyError:
                print("无该地的威妥玛表示")

def main():
    '''功能选择器'''
    desire = input("转换人名[0]\n查找地名[1]: ")
    if '0' == desire:
        name = input('请输入姓名: ')
        character2pinyin(name)
    else:
        district = input('请输入地名(输0显示所有地区威式注音表): ')
        districtSearcher(district)

if __name__ == "__main__":
    main()
