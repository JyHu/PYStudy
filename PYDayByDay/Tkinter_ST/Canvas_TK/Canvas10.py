#coding=utf-8


__author__ = 'JinyouHU'



#使用tag_bind来绑定item与事件

from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')


rt1 = cv.create_rectangle(10,10,110,110,
                          width=8,
                          fill='blue',      #不填充的话，只对点击边框有效
                          tags=('r1','r2','r3'))

def printRect(event):
    print 'rectangle'


#绑定item与事件

cv.tag_bind('r2','<Button-2>',printRect)    #Button-1 左键单击   Button-2  右键单击

cv.pack()

root.mainloop()