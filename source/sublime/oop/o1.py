# 
# coding:utf-8
# 

'''

Python OOP编程学习开始

'''

__author__ = 'JyHu'

# 在Python中定义类是通过class关键字
# 类名通常是大写开头的单词
# 紧接着是（Object），表示该类是从哪个类继承下来的
class Student(object):
	#  __init__ 方法的第一个属性永远都是self
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s : %s' % (self.name, self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'



def max_i(num):
	while(num):
		if num / 10 < 1:
			return num
		num = num / 10		


if __name__ == '__main__':

	bart = Student('Bart Simpson', 59)
	lisa = Student('Lisa', 87)

	bart.print_score()
	lisa.print_score()

	print(bart.get_grade())
	print(lisa.get_grade())

	print(max_i(7))