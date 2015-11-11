# 
# coding:utf-8
# 

'''
单元测试的demo，需要被d6.py引用
'''

__author__ = 'JyHu'


class Dict(dict):
	
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribtue '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value










