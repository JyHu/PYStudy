#coding:utf-8
#
#


name = "Jims"
def reset():
	name = "Mike"
print name


def reset1():
	global name
	name = "Mike"
print name

print callable(str)		# 是否能够被调用

print cmp(1, 4)		# 大小比较
print cmp(3, 2)
print cmp(2, 2)
print cmp("a", "d")

print divmod(10, 3)		# 除法，返回商和余数


print isinstance("abd", str)  # 测试对象的类型
def displayNumType(num):
	print num, 'is'
	if isinstance(num, (int, long, float, complex)):
		print 'a number of type :', type(num).__name__
	else:
		print 'not a number at all'
displayNumType(-71)
displayNumType(13.111)
displayNumType(9999999999999999999999999)
displayNumType(-2234+23j)
displayNumType('adsdf')


print len('aaaaa')		# 计算对象的长度
print len([2, 5, 1])


print pow(2, 4)		# 幂运算


print range(10)
print range(2, 10)
print range(1, 10, 2)	# 参数1：开始值， 参数2：结束值， 参数3：步长	


xr = xrange(10)  	# 类似range，但是只有在需要时才进行计算
print xr[0]
print xr[7]

print round(3.1415926, 4)  # 返回浮点数四舍五入值，参数2：四舍五入的小数位数


print type("a")		# 返回对象的数据类型。
print type([1, 4])
print type(1.4)



##########################################################################################


print chr(65)				# chr返回ASCII对应的字符串
print chr(65) + chr(66)



print float('134')
print hex(161400)	# 转16进制
print oct(13)		# 转8进制
print ord('a')		# 返回参数的ASCII码
print long('123')
print list('Hello world')
print int('35')
print min(1, 6, 9, 0, 3)
print max(7, 3, 1, 9, 0)
print str(13324 + 4j)
print tuple('Hello world')




##########################################################################################


def nobad(s):
	return s.find('bad') == -1
s =['bad', 'good', 'badman', 'nice']
print filter(nobad, s)		# 根据过滤函数对list中得所有数据进行一次过滤


import string
arr = ['python', 'zope', 'linux']
print map(string.capitalize, arr) 	# 将函数作用于list中得每个元素



import operator
n1 = [1, 4, 2]
n2 = [2, 3, 8]
n3 = [4, 5, 1]
print map(operator.mul, n1, n2)
print map(None, n1, n2, n3)


print reduce(operator.mul, n1)
print reduce(operator.mul, n2, 2)	# reduce会取参数中得前两个值进行函数计算，然后将结果与下一个参数一起再进行计算





print zip([1, 2, 3], [4, 5], [6, 7 ,8 ,9])	# 依次合并每组的相同索引位置的值，直到最小的序列合并完。
print zip([1, 2, 3, 4, 5, 6, 7])




for letter in 'Hello world':
	print letter


















