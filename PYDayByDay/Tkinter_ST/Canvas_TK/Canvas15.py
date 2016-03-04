#coding=utf-8


__author__ = 'JinyouHU'


'''

设置弧形的角度

使用start/extent指定起始角度与偏移角度

'''

from Tkinter import *


root = Tk()

cv = Canvas(root, bg='red')
d = {1: PIESLICE, 2: CHORD, 3: ARC}
for i in d:
    cv.create_arc(
        (10, 10 + 60 * (i - 1), 110, 110 + 60 * (i - 1) ),
        style=d[i],
        start=0,    #开始位置为时钟的三点钟方向
        extent=90)  #结束角度，绘图方向为逆时针

cv.create_rectangle(10, 10, 110, 110)

co = ['white','green','blue','pink']

k = 0

def addARC():
    global k
    cv.create_arc((10,10,110,110),
                  style=PIESLICE,
                  start=20 * k,
                  extent=40 * k,
                  fill=co[k % len(co)]
                  # fill=0xFF0011
    )
    k += 1


Button(root, text='addARC', command=addARC).pack()


cv.pack()
root.mainloop()