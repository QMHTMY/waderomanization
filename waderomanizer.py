#!/usr/bin/python
# coding:utf-8
#
# 一键生成中文的威妥玛拼音表示 
# 查找中国城市等地区的威妥玛表示
#
# Author: Shieber
# Date: 2019.07.22
import json
from pypinyin import lazy_pinyin 

def character2pinyin(name):
    pinyin = lazy_pinyin(name) 
    with open('pinyin.json','r') as json_pyin:
        namejson = json.load(json_pyin)
        lgth = len(pinyin)

        if 4 == lgth:
            surname = namejson[pinyin[0]]
            lastnm1 = namejson[pinyin[1]]
            lastnm2 = namejson[pinyin[2]]
            lastnm3 = namejson[pinyin[3]]
            fullnm  = ''.join([surname,' ',lastnm1,' ',lastnm2,' ',lastnm3])
        elif 3 == lgth:
            surname = namejson[pinyin[0]]
            lastnm1 = namejson[pinyin[1]]
            lastnm2 = namejson[pinyin[2]]
            fullnm  = ''.join([surname,' ',lastnm1,' ',lastnm2])
        elif 2 == lgth:
            surname = namejson[pinyin[0]]
            lastnm  = namejson[pinyin[1]]
            fullnm  = ''.join([surname,' ',lastnm])
        elif 1 == lgth:
            char    = namejson[pinyin[0]]
            fullnm  = char 
        else:
            fullnm  = None

    return fullnm 

def districtSearcher():
    '''中国地名的威式拼音搜寻器'''
    pass

def mainControl():
    '''功能选择器'''
    selector = input('转换人名或查找地名[0,1]: ')

    if '0' == selector:
        name = input('请输入姓名: ')
        fullname = character2pinyin(name)
        print(fullname)
    else:
        district  = input('请输入地名(输入0显示所有地区威式注音表): ')
        pass

if __name__ == "__main__":
    mainControl()
