#coding=utf-8

__author__ = 'JinyouHU'


'''

#Pack为一布局管理器，可将它视为一个弹性的容器

root.pack_slaves()
查看当前root下的子组件,解释器没有报异常，说明Pack已创建，并可以使用,此时的输出为空，即root没有任何子组件。

'''


from Tkinter import *

root = Tk()

print root.pack_slaves()

Label(root, text='pack').pack()

print root.pack_slaves()

root.mainloop()