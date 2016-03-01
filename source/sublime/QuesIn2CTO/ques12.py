#coding:utf-8


'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''


import math


# 判断num是否是素数
def isPrimeNum(num):
	for t in range(2, int(math.sqrt(num)) + 1):
		if num % t == 0:
			return False
	return True

# 计算从fro到end间的素数的个数	
def primeNumBetween(fro, end):
	if fro == 1:
		fro = 2
	elif end < 2:
		return []
	pri = []
	for num in range(fro, end + 1):
		if isPrimeNum(num):
			pri.append(num)
	return pri

# 计算从2开始到给定的end之间的素数的个数
def primeNumTo(end):
	return primeNumBetween(2, end)

# 计算规定个数的素数
def primeNumCount(co):
	num = 2
	count = 0
	pri = []
	while count < co:
		if isPrimeNum(num):
			count += 1
			pri.append(num)
		num += 1
	return pri


print primeNumBetween(2, 100)
print primeNumTo(100)
print primeNumCount(5)
print primeNumBetween(101, 200)



