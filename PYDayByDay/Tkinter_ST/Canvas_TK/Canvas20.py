#coding=utf-8


__author__ = 'JinyouHU'


from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')


cv.create_oval((10,10,210,110), #创建椭圆，圆是长宽相等的时候
               outline='blue',width=2)

cv.create_polygon((30,30,30,200,100,170,200,20),    #创建多边形(x,y),(x,y)...
                  outline='green',
                  width=2)

cv.create_text((10,10),     #绘制文字  # 使用anchor控制文字的位置，使用justify控制对齐方式
               text='hello text',
               anchor=W,fill='white')

cv.pack()

root.mainloop()