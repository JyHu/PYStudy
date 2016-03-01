#coding:utf-8




import math



# 判断num是否是素数
def isPrimeNum(num):
	for t in range(2, int(math.sqrt(num)) + 1):
		if num % t == 0:
			return False
	return True

# 获取num的质因数
def getPrimeFactor(num):
	if num < 2:
		print 'To small'
		return []
	if isPrimeNum(num):
		return [num]
	L = []
	temp = num
	while not isPrimeNum(temp):
		for i in range(2, int(math.sqrt(temp)) + 1):
			if (temp % i == 0) and isPrimeNum(i):
				L.append(i)
				temp /= i
				break
	L.append(temp)
	return L


def simpPriNumber(num):
	L = []
	for i in range(1, int(num / 2.0) + 1):
		if num % i == 0:
			L.append(i)
	return L