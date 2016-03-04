#coding=utf-8

__author__ = 'JinyouHU'

from Tkinter import *

'''

绘制弧形
创建一个ARC

'''

root = Tk()
cv = Canvas(root, bg='red')

cv.create_arc((10,10,110,110),fill='blue',outline='green',width=2)
cv.pack()

root.mainloop()