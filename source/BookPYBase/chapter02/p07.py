#coding:utf-8


x = 1
def change_global():
	global x
	x = x + 1
print x
change_global()
print x

y = 1
def change_global1():	# 需要用global来将参数置为全局，否则会造成程序
	y = y + 1
print y 
change_global1()
print y












