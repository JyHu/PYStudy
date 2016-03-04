#coding=utf-8

__author__ = 'JinyouHU'


'''

缩放item
scale缩放item，计算公式：(coords-offset)*scale+offset

'''

from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red', width=300,height=200)

#创建两个rectangle
rt1 = cv.create_rectangle(10,10,110,110,fill='blue')

cv.pack()


def myscale():
    #将y坐标放大为原来的2倍，x坐标不变
    cv.scale(rt1, 0, 0, 1.5, 0.8)

Button(root,text='scale',command=myscale).pack()

root.mainloop()

# scale的参数为(self,xoffset,yoffset,xscale,yscale)