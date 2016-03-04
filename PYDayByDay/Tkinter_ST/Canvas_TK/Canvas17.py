#coding=utf-8


__author__ = 'JinyouHU'

'''

#创建gif图像create_image

'''


from Tkinter import *

root = Tk()

cv = Canvas(root, bg='red')

img = PhotoImage(file='/Users/k/Pictures/MINE/gif/2345245245.gif')
cv.create_image((50, 50), image=img)

cv.pack()
root.mainloop()


'''

gif 动画不动 ……

'''