#coding=utf-8


__author__ = 'JinyouHU'


# 测试measure和metrics属性
from Tkinter import *
import tkFont
root = Tk()
# 创建一个Label
ft1 = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)
Label(root,text = 'hello font',font = ft1 ).grid()

ft2 = tkFont.Font(font = ('Fixdsys','10',tkFont.NORMAL),size = 40)
Label(root,text = 'hello font',font = ft2).grid()

# 得到字体的宽度
print ft1.measure('hello font')
print ft2.measure('hello font')

# 打印两个字体的属性
for metric in ('ascent','descent','linespace','fixed'):
    print ft1.metrics(metric)
    print ft2.metrics(metric)
root.mainloop()
# 使用这两个方法得到已创建字体的相关属性值