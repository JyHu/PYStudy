#coding=utf-8



__author__ = 'JinyouHU'



'''

创建带箭头的直线create_line

'''

from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')
d = [(0,'none'),(1,'first'),(2,'last'),(3,'both')]
for i in d:
    cv.create_line(
        (10, 10+i[0]*20,110,110+i[0]*20),   #设置直线的起始、终点位置
        arrow=i[1],         #设置直线是否使用箭头
        arrowshape='%d %d %d' % (5*i[0], 10*i[0], 10*i[0])  #设置箭头的形状（填充长度，箭头长度，箭头宽度）
    )
cv.pack()

root.mainloop()