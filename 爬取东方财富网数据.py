#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/210:14
# @Author : ZL
# @File : 爬取东方财富网数据.py
# @Software: PyCharm

import requests



#定义一个值存储要查询的股票代码
Numb1 = 600160
#找到网站并访问获取网页内容
def AskHTML():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    response = requests.get('http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?lmt=0&klt=101&secid=1.{}&fields1=f1,f2,f3,f7&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65&ut=b2884a393a59ad64002292a3e90d46a5&cb=jQuery1830062303632186986535_1606017061866&_=1606017062018'.format(Numb1), headers=headers)
    data = response.text.split('["')[1].split('"]')[0].split('","')#数据切片，【0】取前，【1】取后,不添加则按参数分隔
    listdata = [] #分隔后的总列表存储
    riqidata = [] #从总列表中抽取的日期列表，日期下拉列表备用
    for i in range(0,len(data)):
        data1 = list(data[i].split(','))
        listdata.append(data1)  #将处理得到的数据存储到listdata中
    for k in range(0,len(listdata)):
        data2 = list(listdata[k][0].split(','))
        riqidata.append(data2)
    print(riqidata)
    # #创建两个输入项目用来给日期下拉列表备用
    # in1 = input("输入第一个日期：")
    # in2 = input("输入第二个日期：")
    # #定义a1，a2用来定位列表元素的位置
    # a1 =0
    # a2 =0
    # sumlist = []
    # for a in range(0,len(listdata)):
    #     if in1 == listdata[a][0]:
    #         a1 = a
    #     if in2 == listdata[a][0]:
    #         a2 = a
    # #取两值之差，用来确定元素遍历的范围
    # if a1>a2:
    #     tianshu = a1-a2#天数
    #     for b in range(a2,a1+1):
    #         sumdata = float(listdata[b][1])
    #         sumlist.append(sumdata)
    # if a2>a1:
    #     tianshu = a2 - a1#天数
    #     for b in range(a1,a2+1):
    #         sumdata = float(listdata[b][1])
    #         sumlist.append(sumdata)
    # #print(sumlist) #用来测试范围是否正确
    # jieguo = sum(sumlist)/10000 #输出结果进4位
    # return print(str(Numb1)+f"在期间{tianshu+1}天的资金流量为："+str(jieguo)+"万元")


AskHTML()
