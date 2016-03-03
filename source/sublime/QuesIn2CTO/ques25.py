#coding:utf-8


'''

题目：求1+2!+3!+...+20!的和。

'''


def npow(n): 
	if isinstance(n, (int, long)) and (n > 0):
		return reduce(lambda x, y : x + y, map(lambda k : reduce(lambda x, y : x * y, range(1, k + 1)), range(1, n + 1)))
	return 0

print npow(4)



def mpow(n):
	if n == 1: return 1
	return n * mpow(n - 1)
print mpow(3)


def tadd(n):
	def tpow(m):
		if m == 1: return 1
		return m * tpow(m - 1)
	if n == 1: return 1
	return tpow(n) + tadd(n - 1)

print tadd(4)