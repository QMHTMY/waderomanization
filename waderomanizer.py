#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Author: Shieber
#    Date: 2019.07.22
#
#                             APACHE LICENSE
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#                            Function Description
#    一键生成中文的威妥玛拼音表示 
#    查找中国城市等地区的威妥玛表示
#
#    Copyright 2019 
#    All Rights Reserved!

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
            fullnm  = ''.join([surname.title(),' ',lastnm1,' ',lastnm2,' ',lastnm3])
        elif 3 == lgth:
            surname = namejson[pinyin[0]]
            lastnm1 = namejson[pinyin[1]]
            lastnm2 = namejson[pinyin[2]]
            fullnm  = ''.join([surname.title(),' ',lastnm1,' ',lastnm2])
        elif 2 == lgth:
            surname = namejson[pinyin[0]]
            lastnm  = namejson[pinyin[1]]
            fullnm  = ''.join([surname.title(),' ',lastnm])
        elif 1 == lgth:
            char    = namejson[pinyin[0]]
            fullnm  = char 
        else:
            fullnm  = '暂无'

    return fullnm 

def districtSearcher(district):
    '''中国地名的威式拼音搜寻器'''
    if '0' == district:
        with open('diming.json','r') as json_diming:
            diming = json.load(json_diming)
            for k,v in diming.items():
                print(k,v)
    else:
        with open('diming.json','r') as json_diming:
            diming = json.load(json_diming)
            print(diming[district])

def mainControl():
    '''功能选择器'''
    selector = input('转换人名或查找地名[0,1]: ')

    if '0' == selector:
        name = input('请输入姓名: ')
        fullname = character2pinyin(name)
        print(fullname)
    else:
        district  = input('请输入地名(输入0显示所有地区威式注音表): ')
        districtSearcher(district)

if __name__ == "__main__":
    mainControl()
