#coding=utf-8


__author__ = 'JinyouHU'


from Tkinter import *

root = Tk()

root.geometry('80x80+0+0')

print root.pack_slaves()

for i in range(5):
    Label(root, text='pack'+str(i)).pack()

print root.pack_slaves()

root.mainloop()


'''


使用默认的设置pack将向下添加组件，第一个在最上方，然后是一次向下排列。


如果取消root的大小设置，就会显示出全部的label。
这能说明pack为弹性容器


'''