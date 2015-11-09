#
# coding:utf-8
# 
# auth:JyHu
# 


# 函数作为返回值

def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax


def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f =  lazy_sum(1, 3, 5, 7, 9, 11)
print(f)
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# 闭包

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
c1, c2, c3 = count()
print(c1())
print(c2())
print(c3())

def countn():
	def f(j):
		return lambda : j * j
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
cn1, cn2, cn3 = countn()
print(cn1())
print(cn2())
print(cn3())



# 匿名函数 lambda

p = list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(p)

f = lambda x : x * x
print(f)
print(f(6))



def build(x, y):
	return lambda : x ** 2 + y ** 2
v = build(4, 5)
print(v)
print(v())


# Warning ...
# 装饰器（Decorator） 2.7 跑不了

def now():
	print('2015-03-25')
f = now
print(f)
print(now.__name__)		# 函数都可以作为一个对象，函数对象都有一个 __name__ 属性，可以取到函数的名字
print(f.__name__)


def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*arg, **kw)
	return wrapper
@log
def nt():
	print('2015年')
print(nt())








