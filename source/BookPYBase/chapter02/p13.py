#coding:utf-8



__metaclass__ = type

class Rectrangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self, size):
		print 'size'
		self.width , self.height = size
	def getSize(self):
		return self.width, self.height
	# 通过property可以将get、set方法实现成一个成员变量
	size = property(getSize, setSize)

rec = Rectrangle()
print rec.size
rec.size = 1, 3
print rec.width
print rec.height
print rec.size

rec.width = 10
rec.height = 20
print rec.size



