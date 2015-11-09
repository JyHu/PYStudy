
#coding:utf-8

def power(x):
	return x * x

print(power(5))
print(power(55555))

def powerx(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(powerx(4, 4))
print(powerx(2, 30))

print('\n-----------------------------\n')

def powerd(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x

	return s

print(powerd(2))
print(powerd(2, 5))

print('\n-----------------------------\n')

def enroll(name, gener, age = 6, city = 'Beijing'):
	print(name)
	print(gener)
	print(age)
	print(city)
	print('\n')
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city = 'Tianjin')


print('\n-----------------------------\n')

def add_end(L = []):	# 有问题
	L.append('End')
	return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


print('\n-----------------------------\n')


def add_endn(L = None):
	if L is None:
		L = []
	L.append('End')
	return L

print(add_endn())
print(add_endn())
print(add_endn())


print('\n-----------------------------\n')


def calc(numbers):
	um = 0
	for n in numbers:
		um = um + n * n
	return um

print(calc([1, 2, 3, 4, 5]))
print(calc([1, 3, 5, 7, 9]))


print('\n-----------------------------\n')

# 参数前加一个'*' ，表示变参。系统会自动的将多个参数组装成一个tuple元组
def calcm(*nums):
	cou = 0
	for n in nums:
		cou = cou + n
	return cou
print(calcm(1, 3, 5, 7))
print(calcm(2, 4, 6, 8))
print(calcm())

numbs = [1, 2, 3]
print(calcm(*numbs))  # 传变参的	


print('\n-----------------------------\n')

# 关键字参数
# 使用 ** 来实现获取必要参数加可变的其他参数的功能
def person(name, age, **kw):
	print('name:', name, 'age', age, 'other', kw)
person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adam', 45, city = 'London', gender = 'M', job = 'Engineer')

extra = {'city' : 'Beijing', 'job' : 'Engineer'}
person('Jack', 36, **extra)	# 传入一个字典


print('\n-----------------------------\n')


# 命名关键字参数
# 参数列表中间加一个 '*'
# def woker(name, age, *, city, job):
# 	print(name, age, city, job)
# woker('Lucy', 36, city = 'Beijing', job = 'Engineer')




print('\n-----------------------------\n')


# 参数组合
# 
def f1(a, b, c = 0, *arg, **kw):
	print('a =',a, ' b =', b, ' c =', c, ' arg =', arg, ' kw = ', kw)
# def f2(a, b, c = 0, *, d, **kw):
# 	print('a =',a, ' b =', b, ' c =', c, ' d =', d, ' kw = ', kw)

f1(1, 2)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99, k = 88)

arg = (1, 2, 3, 4)
kw = {'d' : 99, 'x' : '#'}
f1(*arg, **kw)
arg2 = (1, 2, 3, 4, 5, 6)
f1(*arg2, **kw)










