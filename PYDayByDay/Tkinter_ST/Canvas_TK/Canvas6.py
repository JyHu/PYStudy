#coding=utf-8

__author__ = 'JinyouHU'


# 使用find_xxx查找上一个或下一个item
from Tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
rt2 = cv.create_rectangle(
    20,20,80,80,
    tags = ('s1','s2','s3'))
rt3 = cv.create_rectangle(
    30,30,70,70,
    tags = ('y1','y2','y3'))
# 查找rt2的上一个item,并将其边框颜色设置为红色
cv.itemconfig(cv.find_above(rt2),outline = 'red')
# 查找rt2的下一个item,并将其边框颜色设置为绿色
cv.itemconfig(cv.find_below(rt2),outline = 'green')

cv.pack()
root.mainloop()