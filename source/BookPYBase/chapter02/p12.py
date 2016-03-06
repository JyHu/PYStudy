#coding:utf-8


__metaclass__ = type

class TestClass():
	def __init__(self):
		super(TestClass, self).__init__()

	def __len__(self):
		'''
		这个方法返回集合中所含项目的数量。
		对于序列来说，就是元素的个数；
		对于映射来说，则是键值对的数量；
		如果返回0，对象会被当做一个布尔变量中得假值进行处理	
		'''
		pass

	def __getitem__(self, key):
		'''
		这个方法返回与所给键对应的值，相当于OC中得KVC	
		'''
		pass

	def __setitem__(self, key, value):
		'''
		相当于OC中得KVC
		'''
		pass

	def __delitem__(self, key):
		'''
		删除元素对应的键值
		'''
		pass



def checkIndex(key):
	'''
	所给的键是能接受的索引吗？
	为了能被接受，键应该是一个非负的整数。
	如果他不是一个整数，会引发TypeError；
	如果他是负数，则会引发IndexError
	'''
	if not isinstance(key, (int, long)):
		raise TypeError
	if key < 0 :
		raise IndexError

class ArithmeticSequence:
	def __init__(self, start = 0, step = 1):
		'''
		初始化算术序列
		起始值---序列中得第一个值
		步长---两个相邻值之间的差别
		改变---用户修改的值得字典
		'''
		self.start = start		# 保存开始值
		self.step = step		# 保存步长值
		self.changed = {}		# 没有项被修改	

	def __getitem__(self, key):
		'''
		'''
		checkIndex(key)

		try:
			return self.changed[key]	# 修改了吗？
		except KeyError:
			return self.start + key * self.step

	def __setitem__(self, key, value):
		'''
		修改算术序列中得一个值
		'''
		checkIndex(key)
		self.changed[key] = value

s = ArithmeticSequence(1, 2)
print s[4]
print s[5]
s[5] = 2
print s[5]
# del s[4]	# 删除的时候会造成程序崩溃，应为没有实现__del__方法
print s['a']












