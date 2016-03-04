#-*- encoding=UTF-8 -*-

__author__ = 'JinyouHU'

from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_here = Button(frame, text="Hello", command=self.say_hi)
        self.hi_here.pack(side=LEFT)

    def say_hi(self):
        print "hi there, every one !"

rt = Tk()
app = App(rt)

rt.mainloop()
