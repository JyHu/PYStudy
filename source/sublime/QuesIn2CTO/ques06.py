#coding:utf-8


'''

题目：斐波那契数列。

'''


def fabi(n):
	L = []
	count = 0
	a, b = 0, 1
	while b < n:
		L.append(b)
		count += 1
		a, b = b, a + b
	return (L, count)

r = fabi(10000)

print r[0]
print r[1]