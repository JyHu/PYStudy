#coding=utf-8

__author__ = 'JinyouHU'


'''

使用tag_bind来绑定item与事件

'''


from Tkinter import *


root = Tk()


cv = Canvas(root, bg='red')

rt1 = cv.create_rectangle(10, 10, 110, 110,
                          width=8,
                          fill='blue',
                          tags=('r1', 'r2'))

def printRect(event):
    print 'rectangle'

def printLine(event):
    print 'line'

cv.tag_bind('r1', '<Button-1>', printRect)
cv.tag_bind('r2', '<Button-2>', printLine)

cv.create_line(10, 150, 100, 200, width=5, tag='r1')
cv.pack()

root.mainloop()