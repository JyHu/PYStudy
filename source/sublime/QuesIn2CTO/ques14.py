#coding:utf-8


'''

题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

'''




import math
import impModule


# # 判断num是否是素数
# def isPrimeNum(num):
# 	for t in range(2, int(math.sqrt(num)) + 1):
# 		if num % t == 0:
# 			return False
# 	return True


# def getPrimeFactor(num):
# 	if num < 2:
# 		print 'To small'
# 		return []
# 	if isPrimeNum(num):
# 		return [num]
# 	L = []
# 	temp = num
# 	while not isPrimeNum(temp):
# 		for i in range(2, int(math.sqrt(temp)) + 1):
# 			if (temp % i == 0) and isPrimeNum(i):
# 				L.append(i)
# 				temp /= i
# 				break
# 	L.append(temp)
# 	return L

def strFac(m, n):
	if isinstance(m, str):
		return "%s * %d" % (m, n) 
	if isinstance(m, (int, long)):
		return "%d * %d" % (m, n)
	return " "

if __name__ == "__main__":

	res = impModule.getPrimeFactor(1048)

	if len(res) == 0:
		print "None"
	else:
		print reduce(strFac, res)





