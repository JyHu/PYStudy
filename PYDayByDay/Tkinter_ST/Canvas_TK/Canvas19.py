#coding=utf-8


__author__ = 'JinyouHU'

'''

创建直线，使用joinstyle属性

'''


from Tkinter import *

root = Tk()

cv = Canvas(root,bg='red')

d = [(0,'none','bevel'),(1,'first','miter'),(2,'last','round'),(3,'both','round')]
for i in d:
    cv.create_line(
        (10,10 + i[0]*20,110,110+ i[0] * 20),   # 设置直线的起始、终点
        arrow = i[1],                           # 设置直线是否使用箭头
        arrowshape = '8 10 3',                  # 设置箭头的形状(填充长度，箭头长度，箭头宽度
        joinstyle = i[2],
        )
cv.pack()
root.mainloop()