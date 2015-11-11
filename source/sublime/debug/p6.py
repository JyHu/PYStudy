# 
# coding:utf-8
# 

'''

'''


__author__ = 'JyHu'

import unittest

from d5 import Dict

# 编写单元测试的时候，需要编写一个测试类，从 unittest.TestCase 继承
class TestDict(unittest.TestCase):

	# 以 test 开头的方法就是测试方法
	# 不以 test 开头的方法不被认为是测试方法，测试的时候不会被执行
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isiinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty




if __name__ == '__main__':
	unittest.main()

