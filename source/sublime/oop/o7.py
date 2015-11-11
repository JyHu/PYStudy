# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'


# __str__

class Student(object):
	def __init__(self, name):
		self.name = name

print(Student('Michael'))


class Student1(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student1 object (name: %s)' % self.name
	__repr__ = __str__

print(Student1('Michael'))

s = Student1('John')
print(Student1)





# __getattr__

class Student2(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self, attr): 	# 当获取一个没有的属性的时候，会到这里来
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda: 25	# 返回一个函数
		else:
			return 'Empty attribute : %s' % attr
		# raise AttributeError('error attribute %s' % attr)

s2 = Student2()
print(s2.name)
print(s2.score)
print(s2.age())
print(s2.grade)






class Chain(object):
	
	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

p = Chain().status.user.timeline.list

print(p)

# print(Chain().users('michael').repos)






# __call__

class Student3(object):
	def __init__(self, name):
		self.name = name

	def __call__(self, hel):
		print('My name is %s. %s' % (self.name, hel))

s3 = Student3('Michael')
print(s3('hello'))


print(callable(Student3('h')))
print(callable('123'))



