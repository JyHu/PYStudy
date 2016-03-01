#coding:utf-8







'''

题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

'''


import string

s = raw_input('please input a string:\n')

letter = 0
number = 0
space = 0
other = 0


for le in s:
	if le.isalpha():
		letter += 1
	elif le.isspace():
		space += 1
	elif le.isdigit():
		number += 1
	else:
		other += 1

print 'letter = %d, number = %d, space = %d, other = %d' % (letter, number, space, other)



