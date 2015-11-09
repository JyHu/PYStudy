# 
# coding:utf-8
# 

'''
访问限制
'''

__author__ = 'JyHu'


class Student(object):
	def __init__(self, name, score):
		self.__name = name 		# 前面添加 ‘__’ 相当于OC中的私有属性了，这时候在外部就无法容易的直接引用
		self.__score = score
	def print_score(self):
		print(self.__score)

	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_name(self, name):
		self.__name = name
	def set_score(self, score):
		try:
			if 0 <= score <= 100:
				self.__score = score
			else:
				raise ValueError('Bad score')
		except ValueError, error:
			print('catch error : %s' % error)


bart = Student('Bart', 89)
bart.print_score()
# print(bart.__score)	# 非法
print(bart.get_score())
bart.set_score(90)
print(bart.get_score())
bart.set_score(-1)
print(bart.get_score())
print(bart._Student__name)  # Python的私有变量其实是编译器把它变成了类名加变量名了









