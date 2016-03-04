#coding=utf-8

__author__ = 'JinyouHU'


from Tkinter import *

root = Tk()

print root.pack_slaves()

L1 = LabelFrame(root,text='pack1',bg='red')

L1.pack(side=LEFT,ipadx=20)
Label(L1,
      text='inside',
      bg='blue').pack(expand=1,side=LEFT)
L2 = Label(root,
           text='pack2',
           bg='blue').pack(fill=BOTH,expand=1,side=LEFT,padx=10)
L3 = Label(root,
           text='pack3',
           bg='green').pack(fill=X,expand=0,side=LEFT,pady=10)


print root.pack_slaves()

root.mainloop()