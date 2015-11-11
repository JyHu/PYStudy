# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print('%s => %s , %s' % (name, member, member.value))