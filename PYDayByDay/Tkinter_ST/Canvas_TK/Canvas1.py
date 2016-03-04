#coding=utf-8

__author__ = 'JinyouHU'

# 提供可以用来进行绘图的Container，支持基本的几何元素，使用Canvas进行绘图时，所有的操作都是通过Canvas，不是通过它的元素
# 元素的表示可以使用handle或tag。


#指定画布的颜色为白色

from Tkinter import *

root = Tk()



#创建一个Canvas，设置其背景色为白色

cv = Canvas(root, bg='white')
cv.pack()


root.mainloop()