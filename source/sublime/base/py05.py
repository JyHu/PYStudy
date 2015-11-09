
#coding:utf-8

import math

print(abs(-100))
print(max(1, 2))
print(str(1.23))
print(bool(1))

a = abs
print(a(-1))
print(hex(255))
print(hex(10000))


def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

# 定义一个空的函数，什么也不做，使用pass
def nop():
	pass

print(my_abs(-8))
# print(my_abs('A'))
# print(my_abs(1, 2))



def my_abs_n(x):
	if not isinstance(x, (int, float)):		# if not 如果不是。 isinstance 是不是某个类型
		raise TypeError('bad operand type')	# 抛出异常
	if x >= 0:
		return x
	else:
		return -x
print(my_abs_n(-9))
print('as')
print((1, 4))




def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

x = move(100, 100, 60, math.pi / 6.0)
print(x)






