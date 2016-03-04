#coding:utf-8



'''

题目：求100之内的素数。

'''

import math

def isprimeN(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0: return False
	return True

def primeTo(num):
	for i in range(2, num + 1):
		if isprimeN(i) == True : print i

if __name__ == '__main__':
	primeTo(100)