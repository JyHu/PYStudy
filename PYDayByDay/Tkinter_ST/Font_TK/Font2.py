#coding=utf-8


__author__ = 'JinyouHU'



# 引入字体模块
import tkFont
from Tkinter import *

root = Tk()
# 创建一个Label
# 指定字体名称、大小、样式
ft = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)
Label(root,text = 'hello sticky',font = ft ).grid()

root.mainloop()
# 使用tkFont.Font来创建字体。