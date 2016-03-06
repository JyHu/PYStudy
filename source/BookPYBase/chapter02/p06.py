#coding:utf-8

fibs = [0, 1]
for i in range(10):
	fibs.append(fibs[-2] + fibs[-1])
print fibs

def square(x):
	'Calulates the square of the number x'
	return x * x
print square(28)
print square.__doc__	# 函数属性
print help(square)

def square1(x):
	return x * x * x;
print help(square1)

