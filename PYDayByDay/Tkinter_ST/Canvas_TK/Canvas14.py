#coding=utf-8

__author__ = 'JinyouHU'


from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')

#扇形，            弓形，     弧形
d = {1:PIESLICE, 2:CHORD, 3:ARC}

for i in d:
    cv.create_arc((10, 10 + 60*i, 110, 110 + 60 * i),style=d[i])
    print i,d[i]

cv.pack()

root.mainloop()