#coding:utf-8


'''
题目：输出9*9乘法口诀表。
'''


for i in range(1, 10):
	s = ''
	for j in range(1, i + 1):
		s += '%d * %d = %-2d   ' % (j, i, i * j)
	print s