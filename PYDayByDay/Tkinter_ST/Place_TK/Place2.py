#coding=utf-8

__author__ = 'JinyouHU'


# 使用in属性来指定放置到的容器是那一个
from Tkinter import *
root = Tk()
root.geometry('800x600')
lb1 = Label(root,text = 'hello Place',fg = 'green')
bt1 = Button(root,text = 'hello Place',fg = 'red')
# 创建一个Label
lb1.place(relx = 0.5,rely = 0.5,anchor = CENTER)

# 在root同创建一个Button，目的是与bt1相比较
bt2 = Button(root,text = 'button in root',fg = 'yellow')
bt2.place(anchor = W)
# 在Label中创建一个Button
bt1.place(in_ = lb1,anchor = W)
root.mainloop()
# 注意bt2放置的位置是在root的(0,0)处，而button1放置的位置是在lb1的(0,0)处，原因是由于bt1使用了in来指定放置的窗口为lb1