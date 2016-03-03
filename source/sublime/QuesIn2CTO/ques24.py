#coding:utf-8


'''

题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

'''



def countNum(num):
	i, j = 1, 1
	nsum = 0.0
	for k in range(num):
		i, j = j, i + j
		nsum += j / (i * 1.0)
	return nsum
print countNum(20)