#coding:utf-8


'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''


import math

for i in range(0, 10000):
	x = int(math.sqrt(i + 100))
	y = int(math.sqrt(i + 168))
	if (math.pow(x, 2) == i + 100) and (math.pow(y, 2) == i + 168):
		print i

