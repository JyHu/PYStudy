#coding=utf-8

__author__ = 'JinyouHU'

#move指定x,y在偏移量


from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')

rt1 = cv.create_rectangle(10,10,110,110,
                          fill='blue',
                          tags=('r1','r2','r3'))
cv.create_rectangle(10,10,110,110,
                    fill='green',
                    tags=('r1','r2','r3'))

#移动rt1
cv.move(rt1, 20, 30)
cv.pack()

root.mainloop()