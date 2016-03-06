#coding:utf-8




'''

通过继承来实现过滤器
python可以多继承

'''


class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']
f = Filter()
f.init()
f.filter = ([1, 2, 3])
print f


s = SPAMFilter()
s.init()
t = s.filter(['SPAM', 'SPAM', 'SPAM', 'ages', 'bacon', 'SPAM', 'SPAMEggs'])
print t