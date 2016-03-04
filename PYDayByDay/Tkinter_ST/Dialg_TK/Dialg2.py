#coding=utf-8

__author__ = 'JinyouHU'


'''

askinteger：输入一个整数值
askfloat：输入一个浮点数
askstring：输入一个字符串

'''


from Tkinter import *
from tkSimpleDialog import *


root = Tk()
root.geometry('220x120+0+0')

reInt = IntVar
reFloat = FloatType
reString = StringVar

def intFunc():
    # 输入一个整数，
    # initialvalue指定一个初始值
    # prompt提示信息
    # title提示框标题
    reInt = askinteger(title = 'prompt',prompt = 'input a integer:',initialvalue = 100)
    LB1['text']=str(reInt)

def floatFunc():
    # 输入一浮点数
    # minvalue指定最小值
    # maxvalue指定最大值，如果不在二者指定范围内则要求重新输入
    reFloat = askfloat(title = 'float',prompt = 'input a float',minvalue = 0,maxvalue = 11)
    LB2.set(str(reFloat))

def stringFunc():
    # 输入一字符串
    reString = askstring(title = 'string',prompt = 'input a string')
    LB3['text']=reString

Button(root, text='integer', command=intFunc).place(x=0,y=0)
Button(root, text='float', command=floatFunc).place(x=80,y=0)
Button(root, text='string', command=stringFunc).place(x=140,y=0)

LB1 = Label(root,text='int value here').place(y=40)
LB2 = Label(root,text='float value here').place(y=60)
LB3 = Label(root,text='string value here').place(y=80)

root.mainloop()
# 返回值为各自输入的值。