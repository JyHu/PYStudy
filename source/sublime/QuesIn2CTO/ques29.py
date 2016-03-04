#coding:utf-8


'''

题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

'''


def bp(n):
	if n == 0: return 0
	print n % 10
	return bp(int(n/10)) + 1

if __name__ == '__main__':
	print bp(2347509234)

