# 
# coding:utf-8
# 
# auth:JyHu
# 


# 
# 首字母设为大写
# 

def resetnames(names):
	def highFirstCh(name):
		return name[0:1].upper() + reduce(lambda x, y : x + y, map(lambda ch : ch.lower(), name[1:]))

	return map(highFirstCh, names)

print(resetnames(['adam', 'LISA', 'barT', 'JACK']))



# 
# 把字符串转换成浮点数
# 

def str2float(S):
	def ch2int(ch):
		return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[ch]
	def str2int(s):
		return reduce(lambda x, y : x * 10 + y, map(ch2int, s))
	ns = S.split('.')
	return str2int(ns[0]) + 0.1 ** len(ns[1]) * str2int(ns[1])

print(str2float('73432.008278467'))



# 
# 数组求积
# 	

def prod(L):
	return reduce(lambda x, y : x * y, L)
print(prod([3, 5, 7, 9]))




