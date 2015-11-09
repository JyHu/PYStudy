#!/usr/bin/env python2 			
# -*- coding: utf-8 -*-			

# 第一行表示运行的环境
# 第二行表示编码格式为UTF-8

' a test module '		# 模块的注释，任何模块的第一个字符串都被视为模块的文档注释

__author__ = 'JyHu'		# __author__变量存储作者

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world !')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')


def _private_1(name):
	return 'Hello, %s' % name
def _private_2(name):
	return 'Hi, %s' % name
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)


if __name__ == '__main__':
	test()
	print(greeting('Michael'))
	print(greeting('Joy'))
	print(sys.path)


