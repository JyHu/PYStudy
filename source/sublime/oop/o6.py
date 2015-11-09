# 
# coding:utf-8
# 

'''
多继承(MixIn)
'''

__author__ = 'JyHu'


class Animal(object):
	def sintro(self):
		print("I'm an Animal.")

class Mammal(Animal):
	def introduce(self):
		print("I'm Mammal .")
class Bird(Animal):
	pass
class Runnable(object):
	def run(self):
		print('Running ...')
class Flyable(object):
	def fly(self):
		print('Flying ...')

class Dog(Mammal, Runnable):
	pass
class Bat(Mammal, Flyable):
	pass
class Parrot(Bird):
	pass
class Ostrich(Bird):
	pass



d = Dog()
d.run()
d.introduce()
d.sintro()

print('')

b = Bat()
b.fly()
b.introduce()
b.sintro()
# b.run()





