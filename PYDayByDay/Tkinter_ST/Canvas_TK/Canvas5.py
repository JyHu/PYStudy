#coding=utf-8

__author__ = 'JinyouHU'


#得到了tag值也就得到了这个item，可以对这个item进行相关的设置

from Tkinter import *

root = Tk()

cv = Canvas(root,bg='red')

#使用tags指定一个tag
rt = cv.create_rectangle(10,10,110,110,
                         fill='green',
                         tags=('r1','r2','r3'))
cv.pack()

cv.create_rectangle(20,20,80,80,fill='pink',tags='r3')

#将所有与tag('r3)绑定的item边框颜色设置为蓝色

for item in cv.find_withtag('r2'):
    cv.itemconfig(item, outline='blue',width=5)

root.mainloop()