#coding=utf-8

__author__ = 'JinyouHU'
from Tkinter import *
root = Tk()
border = [0, 2, 4, 6, 8, 2, 4, 8]
i = 0

for a in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
    Button(
        root,
        text = 'anchor',
        anchor = a,
        fg='red',
        bg='red',
        width=30,
        bd=border[i],
        state='disabled',       #'normal','active','disabled'
        height = 4
    ).pack()
    i += 1

root.mainloop()

