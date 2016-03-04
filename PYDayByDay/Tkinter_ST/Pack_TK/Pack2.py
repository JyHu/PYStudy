#coding=utf-8


__author__ = 'JinyouHU'



from Tkinter import *

root = Tk()

#改变root的大小为80×80
root.geometry('80x80+0+0')
print root.pack_slaves()

Label(root, text='pack').pack()
print root.pack_slaves()

root.mainloop()


'''


可以看出Pack的结果没有什么变化，它不对root产生影响
也就是说Pack尅缩小至只包含一个Label组件
root可以自己控制自己的大小


'''