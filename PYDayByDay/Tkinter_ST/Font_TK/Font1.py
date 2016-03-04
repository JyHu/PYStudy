#coding=utf-8

__author__ = 'JinyouHU'



# 改变组件的显示字体
from Tkinter import *
root = Tk()
# 创建一个Label
for ft in ('Arial',('Courier New',),('Comic Sans MS',),'Fixdsys',('MS Sans Serif',),('MS Serif',),'Symbol','System',('Times New Roman',),'Verdana'):
    Label(root,text = 'hello sticky   中文',font = ft ).grid()

root.mainloop()
# 在Windows上测试字体显示，注意字体中包含有空格的字体名称必须指定为tuple类型。