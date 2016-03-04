#coding=utf-8

__author__ = 'JinyouHU'


'''
创建一个矩形，指定画布的颜色为白色
'''

from Tkinter import *


root = Tk()

#创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')

#创建一个矩形，坐标为（10, 10, 110, 110）
# cv.create_rectangle(10, 10, 110, 110)
cv.create_rectangle(
    10,
    10,
    110,
    110,
    fill='red',         #内部填充色，可选
    outline='green',     #外框颜色，可选
    width=5,             #外框宽度，可选
    dash=10,            #指定虚线，可选
)
cv.pack()

cv.create_rectangle(120, 10, 220, 110,
        outline='red',
        stipple='gray12',       #使用画刷填充，使用属性stippe
        fill='green'
)


#记录一个控件
rt = cv.create_rectangle(10, 120, 110, 220,
        outline='red',
        stipple='gray12',
        fill='green'
)
cv.coords(rt,(120, 120, 220, 220))  #重新设置控件位置


root.mainloop()