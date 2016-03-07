#coding:utf-8


class InterceptClass:
	def __init__(self):
		pass
	def __getattribute__(self, name):
		pass
	def __getattr__(self, name):
		pass
	def __setattr__(self, name, value):
		pass
	def __delattr__(self, name):
		pass


class Rectangle:

	'''
	测试__doc__内建方法，一个放置在类前的字符串会被认为是类说明的文字，可以用__doc__方法获取
	'''

	def __init__(self):
		self.width = 0
		self.height = 0
		print 'init'
	def __setattr__(self, name, value):
		if name == 'size':
			self.width, self.height = value
		else:
			self.__dict__[name] = value
	def __getattr__(self, name):
		if name == 'size':
			return self.width, self.height
		else:
			print name + ' is not found'

	def __str__(self):
		if self.width == 0 and self.height == 0 :
			return self.__doc__
		else:
			return 'self.width = %d, self.height = %d' % (self.width, self.height)



r = Rectangle()
print r
r.size = 3, 4 
print r.width
print r.height
print r.size
print r
