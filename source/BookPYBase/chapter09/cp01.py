#coding:utf-8


__metaclass__ = type


class MyClass:
	def __init__(self):
		super(MyClass, self).__init__()
		self.smeth()
		self.cmeth()
		self.tmeth()
	def smeth():
		print 'This is a static method'
	smeth = staticmethod(smeth)
	def cmeth(cls):
		print 'This is a class method of', cls
	cmeth = classmethod(cmeth)
	def tmeth(self):
		print 'This is a member method'

	@staticmethod
	def psmeth():
		print 'This is a static method'

	@classmethod
	def pcmeth(cls):
		print 'This is a class method'


'''


使用staticmethod(mtd)和classmethod(mtd)来定义静态方法和类方法的方式，
使用装饰器也可以例如 @staticmethod @classmethod


'''



mc = MyClass()
mc.smeth()
mc.cmeth()
MyClass.smeth()
MyClass.cmeth()
# MyClass.tmeth()