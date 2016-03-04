#coding=utf-8

__author__ = 'JinyouHU'


#使用addtag_来向上一个或下一个item添加tag
from Tkinter import *

root = Tk()

cv = Canvas(root, bg='white')
rt1 = cv.create_rectangle(10, 10, 110, 110,
                          fill='red',
                          tags=('r1','r2','r3'))
rt2 = cv.create_rectangle(20,20,80,80,
                          fill='green',
                          tags=('s1','s2','s3'))
rt3 = cv.create_rectangle(30,30,70,70,
                          fill='pink',
                          tags=('y1','y2','y3'))

#向rt2的上一个item添加r4
cv.addtag_above('r4',rt2)

#向rt2的下一个item添加r5
cv.addtag_below('r5',rt2)

for item in [rt1, rt2, rt3]:
    print cv.gettags(item)

cv.pack()
root.mainloop()