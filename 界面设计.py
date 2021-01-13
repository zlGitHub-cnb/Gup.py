#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/210:36
# @Author : ZL
# @File : 界面设计.py
# @Software: PyCharm

from tkinter import ttk
import tkinter as tk
import serial.tools.list_ports
from tkinter import scrolledtext,END
import requests

#定义一个值存储要查询的股票代码

listdata = []
riqidata = []

#找到网站并访问获取网页内容

def AskHTML():
    '''
    接收文本框股票代码，并访问网页获取所需数据
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    response = requests.get('http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?lmt=0&klt=101&secid={}&fields1=f1,f2,f3,f7&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65&ut=b2884a393a59ad64002292a3e90d46a5&cb=jQuery1830062303632186986535_1606017061866&_=1606017062018'.format(Send_Window.get()), headers=headers)
    data = response.text.split('["')[1].split('"]')[0].split('","')
    for i in range(0,len(data)):
        data1 = list(data[i].split(','))
        listdata.append(data1)  #将处理得到的数据存储到listdata中
    for k in range(0,len(listdata)):
        data2 = list(listdata[k][0].split(','))
        riqidata.append(data2)
    #创建两个输入项目用来给日期下拉列表备用
    in1 = riqi_Window1.get()
    in2 = riqi_Window2.get()
    #定义a1，a2用来定位列表元素的位置
    a1 =0
    a2 =0
    sumlist = []
    for a in range(0,len(listdata)):
        if in1 == listdata[a][0]:
            a1 = a
        if in2 == listdata[a][0]:
            a2 = a
    #取两值之差，用来确定元素遍历的范围
    if a1>a2:
        tianshu = a1-a2#天数
        for b in range(a2,a1+1):
            sumdata = float(listdata[b][1])
            sumlist.append(sumdata)
    if a2>a1:
        tianshu = a2 - a1#天数
        for b in range(a1,a2+1):
            sumdata = float(listdata[b][1])
            sumlist.append(sumdata)
    #print(sumlist) #用来测试范围是否正确
    jieguo = sum(sumlist)/10000 #输出结果进4位
    # Receive_Window.insert("end",Riqi_Range)
    # Receive_Window.see("end")
    return str(Send_Window.get())+f"在{tianshu+1}天内资金流量："+str(jieguo)+" 万"

def Riqi_Range():
    '''返回一个字符串，已禁用'''
    return str(f"只能选取日期:\n"+f"***{str(riqidata[len(riqidata)-1])}***\n"+"至\n"+f"***{str(riqidata[0])}***")





SerialPort = serial.Serial()
GUI = tk.Tk()  # 父容器
GUI.title("***股票资金辅助查询***")  # 父容器标题
GUI.geometry("450x320+1800+1000")  # 父容器大小
GUI.resizable(0,0)#禁止调整大小

Information = tk.LabelFrame(GUI, text="资金状况", padx=10, pady=10)  # 水平，垂直方向上的边距均为10
Information.place(x=240, y=20)
Information_Window = scrolledtext.ScrolledText(Information, width=20, height=5, padx=10, pady=10, wrap=tk.WORD)
Information_Window.grid()

Send = tk.LabelFrame(GUI, text="股票代码", padx=10, pady=5)  # 水平，垂直方向上的边距均为 10
Send.place(x=15, y=20)


DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
EntrySend = tk.StringVar()
Send_Window = ttk.Entry(Send, textvariable=EntrySend, width=23)
Send_Window.grid()

def WriteData():
    '''
    在屏幕中显示内容
    :return:
    '''
    global DataSend
    DataSend = EntrySend.get()
    Information_Window.insert("end",AskHTML())#
    Information_Window.see("end")


def DeleteData():
    '''
    清除屏幕功能
    :return:
    '''
    Information_Window.delete(1.0,END)
    # Receive_Window.delete(1.0,END)



Receive = tk.LabelFrame(GUI, text="备注：", padx=10, pady=10)  # 水平，垂直方向上的边距均为 10
Receive.place(x=240, y=130)
Receive_Window = scrolledtext.ScrolledText(Receive, width=20, height=9, padx=10, pady=10, wrap=tk.WORD)
Receive_Window.insert("end","股票输入规则:\n深A：0.00xxxx\n沪A：1.60xxxx\n\n日期输入规则：\nxxxx-xx-xx（年月日）\n例如：2020-10-10")
Receive_Window.see("end")
Receive_Window.grid()


option = tk.LabelFrame(GUI, text="日期输入", padx=10, pady=10)  # 水平，垂直方向上的边距均为10
option.place(x=15, y=75, width=191)  # 定位坐标
ttk.Label(option, text="开始日期:").grid(column=0, row=1)
ttk.Label(option, text="停止日期:").grid(column=0, row=2)
riqiSend1 = tk.StringVar()
riqiSend2 = tk.StringVar()
riqi_Window1 = ttk.Entry(option, textvariable=riqiSend1, width=15)
riqi_Window1.grid(column=1, row=1)
riqi_Window2 = ttk.Entry(option, textvariable=riqiSend2, width=15)
riqi_Window2.grid(column=1, row=2)


option = tk.LabelFrame(GUI, text="选项", padx=10, pady=10)  # 水平，垂直方向上的边距均为10
option.place(x=15, y=165, width=191)  # 定位坐标
tk.Button(option, text="开始统计", command=WriteData,width=10).grid(column=0, row=0)
tk.Button(option, text="清屏", command=DeleteData,width=10).grid(column=1, row=0)

img = tk.LabelFrame(GUI, text="作者", padx=10, pady=10)
img.place(x=15, y=240,width=191)
label_img = tk.Label(img,text='阿 包 出 品',bg='black',font=('华文楷体', 22),fg='yellow')
label_img.grid(column=0, row=0)

if __name__ == '__main__':
    GUI.mainloop()



