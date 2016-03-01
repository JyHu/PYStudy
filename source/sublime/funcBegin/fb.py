
#coding:utf-8



def fib(n):
	res = []
	a, b = 0, 1
	while b < n:
		res.append(b)
		a, b = b, a + b
	return res

print fib(100000000)


def cheeseshop(kind, *arguments, **keywords):
	print kind
	for arg in arguments:
		print arg
	for kw in keywords.keys():
		print kw + ' : ' + keywords[kw]

cheeseshop('Hello', 1, 2, 3 ,4, 8, 0, a = '3')
cheeseshop('World', 'a', 'b', 'v', key = 'dictkey')

