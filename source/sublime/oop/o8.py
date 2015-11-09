# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'


# __iter__

class Fib(object):

	def __init__(self):
		self.a, self.b = 0, 1 	# 初始化两个计数器a, b

	def __iter__(self):
		return self 	# 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a < 1000000:
			return self.a
		print('Stop')
		raise StopIteration()

		# try:
		# 	self.a, self.b = self.b, self.a + self.b
		# 	if self.a > 1000000:
		# 		raise StopIteration('Top') # 退出循环的条件
		# 	return self.a 	# 返回下一个值
		# except StopIteration, error:
		# 	print('Stop in %s' % error)

	def __getitem__(self, r):	# 扩展了下标的属性 a[1]
		if isinstance(r, int):	# n 是索引
			m, n = 1, 1
			for x in range(r):
				m, n = n, m + n
			return m
		if isinstance(r, slice): 	# 提供切片功能
			start = r.start
			stop = r.stop
			step = r.step
			if start is None:
				start = 0
			if step is None:
				step = 1
			m, n = 1, 1
			L = []
			for x in range(stop):
				if x >= start and (x - start) % step == 0:
					L.append(m)
				m, n = n, m + n
			return L

f = Fib()
# for x in Fib():
# 	print(x)
for i in range(101):
	print('%d - %d' % (i, f[i]))

print(f[10:15])
print(f[:100:10])











