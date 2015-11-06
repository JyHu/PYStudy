
#coding:utf-8

import math

def quadratic(a, b, c):
	try:
		for x in (a, b, c):
			if not isinstance(x, (int, float)):
				raise TypeError('type error ....')	# 抛出异常

		print('center')

		if a == 0 :
			print('不是一元二次方程')
		elif (b ** 2 - 4 * a * c) < 0:
			print('无解')
		else:
			t = b ** 2 - 4 * a * c
			d = math.sqrt(abs(b ** 2 - 4 * a * c))
			return (-b - d) / 2.0 / a , (-b + d) / 2.0 / a
	except TypeError, errorInfo:	# 第一个参数为异常的类型，后面跟的是raise的异常信息
		print(errorInfo)
	finally:
		pass

print('t1:')
print(quadratic('a', -3, 'c'))
print('\nt2:')
print(quadratic(2, 3, 1))
print('\nt3:')
print(quadratic(1, 3, -4))
print('\nt4:')
print(quadratic(1, 3, 4))	# 无解
print('\nt5:')
print(quadratic(0, 3, 4))	# 一元一次方程
