#coding=utf-8


__author__ = 'JinyouHU'


#delete删除给定的item

from Tkinter import *

root = Tk()

def deleteRT():
    #使用id删除rt1
    cv.delete(rt1)

    #使用tag删除rt2
    cv.delete('s1')

Button(root,text='set',command=deleteRT).pack()

cv = Canvas(root, bg='red')

#创建两个Rectangle
rt1 = cv.create_rectangle(10,10,110,110,fill='green',tags=100)
rt2 = cv.create_rectangle(20,20,130,130,fill='blue',tags='s1')  #最好用英文tag

cv.pack()

root.mainloop()