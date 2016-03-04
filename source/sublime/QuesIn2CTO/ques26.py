#coding:utf-8


'''

题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

'''


def reverse(tstr = 'Hello World'):
	if len(tstr) == 0 : return
	print tstr[-1:]
	reverse(tstr[0:len(tstr) - 1])

reverse(raw_input('please input a string :\n'))