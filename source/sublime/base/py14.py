# 
# coding:utf-8
# 
# auth:JyHu
# 
# 重要 ！！！！！！！！！！！！
# 


# 偏函数

print(int('12345'))

print(int('123456', base = 8))
print(int('1024', base = 16))

def int2(x, base = 2):
	return int(x, base)
print(int2('10000000'))
print(int2('10110111001'))
print(int2('101412', 8))


import functools

int3 = functools.partial(int, base = 2)
print(int3('100000000'))
print(int3('1001010101'))



max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

# 相当于
args = (10, 5, 11, 7)
print(max(*args))
TestModule

# new_func = functools.partial(func, *args, **kw)


def my_partial(func, *args_base, **kw_base):
	def func_new(*args, **kw):
		args_new = []
		for i in args:
			args_new.append(i)
		for i in args_base:
			args_new.append(i)
		kw_new = dict(kw_base)
		kw_new.update(kw)
		return func(*args_new, **kw_new)
	return func_new


def say():
	print('Hello')

def say2(func, peo):
	func()
	print(peo)
say2(say, ' All')





 