# 
# coding:utf-8
# 

'''
继承和多态
'''


__author__ = 'JyHu'


class Animal(object):
	def run(self):
		print('Animal is running ...')

class Dog(Animal):
	def run(self):
		print('Dog is running ...')
	def eat(self):
		print('Eating meat ...')

class Cat(Animal):
	def run(self):
		print('Cat is running ...')

class Husky(Dog):
	def run(self):
		print('Husky is running ...')

def run_twice(animal):
	animal.run()
	animal.run()

dog = Dog()
dog.run()
cat = Cat()
cat.run()
husky = Husky()
husky.run()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

run_twice(dog)
run_twice(Animal())
run_twice(cat)




'''
获取对象信息
'''


print(type(123))
print(type('string'))
print(type(None))
print(type(True))
print(type(abs))
print(type(dog))



print(type(123) == type(456))
print(type(123) == int)
print(type('123') == type('abc'))
print(type('abc') == str)
print(type('123') == type(123))



# 使用types模块中定义好的常量
import types

def fn():
	pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)



# 可以判断几种类型，判断结果是关系是‘或’
print(isinstance(husky, (Dog, Animal, Husky)))
print(isinstance(husky, (Cat, Husky)))



f = dir('ABC')
print('f type %s' % type(f))
for t in f:
	print("'%s' type '%s'" % (type('ABC'), t))
print(len('ABC'))
# 等价于 
print('ABC'.__len__())



class MyDog(object):
	def __len__(self):
		return 100
ndog = MyDog()
print(len(ndog))





class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x ** 2

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
# print(obj.z)	# obj 没有 ‘z’ 属性，直接取用会报错
print(getattr(obj, 'z', 404)) 	# 可以附加参数，返回空值时的默认的值

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())

'''
最好是只有在不知道对象信息的时候，采取获取对象的信息的方法
'''










