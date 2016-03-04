#coding=utf-8

__author__ = 'JinyouHU'
from Tkinter import *
root = Tk()
b1 = Button(root, text='30×1', width=30, height=2)
b1.pack()

b2 = Button(root, text='30×2')
b2['width'] = 30
b2['height'] = 3
b2.pack()

b3 = Button(root, text='30×3')
b3.configure(width=30, height=3)
b3.pack()

root.mainloop()