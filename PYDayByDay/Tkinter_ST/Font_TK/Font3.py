#coding=utf-8


__author__ = 'JinyouHU'



# 使用系统已有的字体显示
from Tkinter import *
import tkFont
root = Tk()
# 创建一个Label
# 指定字体名称、大小、样式
# 名称是系统可使用的字体
ft1 = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)
Label(root,text = 'hello sticky',font = ft1 ).grid()

ft2 = tkFont.Font(font = ('Fixdsys','10',tkFont.NORMAL),size = 40)
Label(root,text = 'hello sticky',font = ft2).grid()

root.mainloop()
# 创建字体有font等其它属性，
# 如果font指定了，有几个参数将不再起作用，如：family,size,weight,slant,underline,overstrike
# 例子中演示的结果是ft2中字体大小为10，而不是40