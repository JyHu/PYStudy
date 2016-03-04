#coding=utf-8


__author__ = 'JinyouHU'


from Tkinter import *


root = Tk()
root.geometry('80x80+0+0')

print root.pack_slaves()

Label(root,text='pack1',bg='red').pack(fill=Y,expand=1,side=LEFT)
Label(root,text='pack2',bg='blue').pack(fill=BOTH,expand=1,side=RIGHT)
Label(root,text='pack3',bg='green').pack(fill=X,expand=0,side=LEFT)
#fill指定填充的方向
#expand 指定在超过空间大小的时候是否拉伸
#side 指定在父视图上的位置

print root.pack_slaves()

root.mainloop()