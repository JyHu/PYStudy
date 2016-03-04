#coding=utf-8


__author__ = 'JinyouHU'


# SimpleDialog：创建一个模态对话框
from Tkinter import *
# 引入SimpleDialog模态对话框
from SimpleDialog import *

root = Tk()
# 创建一个SimpleDialog
# buttons:显示的按钮
# default:默认选中的按钮

def showDia():
    dlg = SimpleDialog(root,
                   text = 'hello SimpleDialog',
                   buttons = ['Yes','No','cancel'],
                   default = 0,
                   )
    # 执行对话框
    print dlg.go()

Button(root,text='show dialg',command=showDia).pack()

root.mainloop()
# 返回值为点击的按钮在buttons中的索引值