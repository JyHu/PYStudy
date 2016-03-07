#coding:utf-8



'''
使用内建的迭代器方法来实现斐波那契
'''

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		return self.b
	def __iter__(self):
		return self
fibs = Fibs()
for i in range(1, 10):
	print fibs.next()

print 2**30

'''


note:

3.0以后迭代器方法做了修改。

				3.0以前		 	 3.0以后
需实现的方法		next			__next__
使用迭代器 	  obj.next()		next(obj)


'''


# 内建的iter也能从对象中获得迭代器
it = iter([1, 2, 3])
print it.next()
print it.next()





###############################################################################
# 从迭代器得到序列


class TestIterator:
	value = 0
	def next(self):
		self.value += 1
		if self.value > 20:
			raise StopIteration
		return self.value
	def __iter__(self):
		return self
ti = TestIterator()
print ti.value
print ti.next()
print ti.next()
print ti.next()
print list(ti)
# print ti.next()
# print ti.next()
# print ti.next()
















