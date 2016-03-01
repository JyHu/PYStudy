#coding:utf-8




'''

题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

'''




from impModule import simpPriNumber

def madd(x, y):
	return x + y

def perfactNum():
	L = []
	for i in range(2, 1000):
		t = simpPriNumber(i)
		if reduce(madd, t) == i:
			L.append(i)
			print i, t
	return L
				
print perfactNum()



