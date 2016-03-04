#coding=utf-8

__author__ = 'JinyouHU'

'''4.控件焦点问题
创建三个Button，各自对应回调函数；将第二个Button设置焦点，程序运行是按“Enter”，判断
程序的打印结果
'''
from Tkinter import *

def cb1():
    print 'buttont 1 clicked'

def cb2(event):
    print 'button 2 clicked'

def cb3():
    print 'button 3 clicked'

def eventInfo(event):
    print 'event.time = ', event.time
    print 'event.type = ', event.type
    print 'event.widgetId = ', event.widget
    print 'event.KeySymbol = ',event.keysym

root = Tk()

b1 = Button(root, text='button1', command=cb1)
b2 = Button(root, text='button2')
b2.bind('<Return>', eventInfo)
b3 = Button(root, text='button3', command=cb3)

b1.pack()
b2.pack()
b3.pack()

b2.focus_set()
root.mainloop()