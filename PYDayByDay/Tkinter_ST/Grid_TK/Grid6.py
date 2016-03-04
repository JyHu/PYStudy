#coding=utf-8


__author__ = 'JinyouHU'



'''8.设置表格中组件的对齐属性'''

# 使用sticky设置对齐方式
from Tkinter import *
root = Tk()
# 创建两个Label
Label(root,text = 'hello sticky').grid()
Label(root,text = 'Tkinter').grid()
# 创建两个Label，并指定sticky属性
Label(root,text = 'hello sticky').grid(sticky = W)
Label(root,text = 'Tkinter').grid(sticky = W)

root.mainloop()
# 默认属性下，组件的对齐方式为居中，设置sticky属性可以控制对齐方式，可用的值（N,S,E,W)及其组合值