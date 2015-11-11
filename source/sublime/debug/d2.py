# 
# coding:utf-8
# 

'''
抛出异常
'''

__author__ = 'JyHu'





if 0:

	class FooError(ValueError):
		pass

	def foo(s):
		n = int(s)
		if n == 0:
			raise FooError('invalid value : %s' % s)
		return 10 / n

	foo('0')

elif 1:
	def foo(s):
		n = int(s)
		if n == 0:
			raise ValueError('invalid value: %s' % s)
		return 10 / n

	def bar():
		try:
			foo('0')
		except ValueError as e:
			print('ValueError !')
			raise

	bar()

