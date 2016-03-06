#coding:utf-8

__metaclass__ = type


class bird():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaaah...'
			self.hungry = False
		else : print "No, thanks, I'm full"
	def __del__(self):	# 内建的销毁函数，当被消费的时候，会自动的调用这个方法
		print 'delete'


class songBird(bird):
	def __init__(self):
		# 如果父类没有实现super方法，那么在这里使用super方法会造成程序崩溃
		# 只需要在最前面添加一个metaclass的说明就行
		super(songBird, self).__init__()
		self.sound = 'guaguagua'
	def sing(self):
		print self.sound

b = bird()
b.eat()
b.eat()

s = songBird()
s.sing()
