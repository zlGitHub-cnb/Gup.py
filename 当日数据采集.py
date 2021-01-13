#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/229:40
# @Author : ZL
# @File : 当日数据采集.py
# @Software: PyCharm

import json
#1.找到网站并访问获取网页内容
host_Html = 'http://data.eastmoney.com/zjlx/{}.html'


def AskHTML():
    import requests

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }



    response = requests.get(
        'http://stockpage.10jqka.com.cn/spService/600160/Funds/realFunds/free/1/',
        headers=headers)
    resp_dict = json.loads(response.text)
    datas = resp_dict.get('title').get('je')
    print(response.text)
    # try:
    #     if response.status_code ==200:
    #         return datas
    #     else:
    #         print('请求失败')
    # except:
    #     return False

if __name__ == '__main__':
    print(AskHTML())
    # Proc_data()