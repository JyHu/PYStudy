#coding=utf-8


__author__ = 'JinyouHU'


#使用tab_bind来绑定item与事件


from Tkinter import *

root = Tk()

cv = Canvas(root,bg='red')

rt = cv.create_rectangle(10, 10, 110, 110,
                         width=8,
                         fill='blue',
                         tags='r1')

def printRect(event):
    print 'rectangle'
def printLine(event):
    print 'line'

#绑定item与左键事件
cv.tag_bind('r1','<Button-1>',printRect)

#绑定item与右键事件
cv.tag_bind('r1','<Button-2>',printLine)

cv.pack()

root.mainloop()