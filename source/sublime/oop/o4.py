# 
# coding:utf-8
# 

'''
__slots__
'''


__author__ = 'JyHu'



class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)	# 给实例绑定一个方法
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(26) 	# 给实例s1绑定的实例方法对于实例s2是不管用的

def set_score(self, score):
	self.score = score
Student.set_score = MethodType(set_score, Student)
s.set_score(89)
s2.set_score(90)
print(s.score)
print(s2.score)		# 结果都是90




class Animal(object):

	# 用tuple定义允许绑定的属性名称
	# 使用slots限制的属性只对当前类实例起作用
	# 对继承的子类是不起作用的
	__slots__ = ('name', 'age') 	

a = Animal()
a.name = 'dog'
a.age = 2
# a.place = 'America'

class Cat(Animal):
	pass
c = Cat()
c.place = 'China'














