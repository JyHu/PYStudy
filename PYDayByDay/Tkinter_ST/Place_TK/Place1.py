#coding=utf-8


__author__ = 'JinyouHU'


from Tkinter import *

root = Tk()

lb = Label(root,text='hello place')

lb.place(x=0, y=0, anchor=NW)

lb2 = Label(root, text='hello place 2')

lb2.place(relx=0.5, rely=0.5, anchor=CENTER)

v = IntVar()
for i in range(5):
    Radiobutton(
        root,
        text='Radio' + str(i),
        variable=v,
        value=i
    ).place(x = 80*i, rely=0.3, anchor=NW)

root.mainloop()
