
#coding=utf-8

__author__ = 'JinyouHU'


# 最后使用两个place方法来动态改变两个Frame的大小。
from Tkinter import *
root = Tk()
split = 0.5
fm1 = Frame(root,bg = 'red')
fm2 = Frame(root,bg = 'blue')
# 单击fm1时增大它的占有区域0.1
def incFm1(event):
    global split
    if split < 1:
        split += 0.1
    fm1.place(rely = 0,relheight = split,relwidth = 1)
    fm2.place(rely = split,relheight = 1 - split,relwidth = 1)
# 单击fm2时增大它的占有区域0.1
def incFm2(event):
    global split
    if split > 0:
        split -= 0.1
    fm1.place(rely = 0,relheight = split,relwidth = 1)
    fm2.place(rely = split,relheight = 1 - split,relwidth = 1)

# 这两语句要使用，不然开始看不到两个frame，也就没法点击它们了
fm1.place(rely = 0,relheight = split,relwidth = 1)
fm2.place(rely = split,relheight = 1 - split,relwidth = 1)
# 绑定单击事件
fm1.bind('<Button-1>',incFm1)
fm2.bind('<Button-1>',incFm2)

root.mainloop()
# 为SplitWindow的原型了，再改动一下就可以实现一个SplitWindow了。