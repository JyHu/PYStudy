#coding=utf-8

__author__ = 'JinyouHU'


'''

使用bitmap创建位图
create_bitmap

'''

from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')
d = {1: 'error', 2: 'info', 3: 'question', 4:'hourglass'}

for i in d:
    cv.create_bitmap((20 * i, 20 * i), bitmap=d[i])

cv.pack()

root.mainloop()