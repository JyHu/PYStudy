# 
# coding:utf-8
# 

'''
测试 type()，需要引用 o10.py
'''

__author__ = 'JyHu'


from o10 import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# type()函数既可以返回一个对象的类型，又可以创建出信的类型，
# 比如，我们可以通过 type()函数创建出Hello类，而无需通过class Hello(object) ... 的定义
def fn(self, name = 'world'):
	print('Hello, %s' % name)
Hello1 = type('Hello1', (object), dict(hello = fn))
h1 = Hello1()
h1.hello()

