
#coding:utf-8

import math

def quadratic(a, b, c):
	print('\n\n')
	for p in (a, b, c):
		print('cycle %s' % p)
		if not isinstance(p, (int , float)):
			raise TypeError('Type error')

	print('center')

	if a == 0 :
		print('不是一元二次方程')
	elif (b ** 2 - 4 * a * c) < 0:
		print('无解')
	else:
		t = b ** 2 - 4 * a * c
		d = math.sqrt(abs(b ** 2 - 4 * a * c))
		return (-b - d) / 2.0 / a , (-b + d) / 2.0 / a


v = quadratic('b', -3, 'a')
print(v)
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(1, 3, 4))	# 无解
print(quadratic(0, 3, 4))	# 一元一次方程
