#coding:utf-8



print '\n'
print '#' * 60
print 'random'
print '#' * 60
print '\n'


import random

print random.random()	# 产生一个伪随机数	
print random.getrandbits(10)	# 产生一个指定进制的伪随机数
print random.randrange(2000, 1000000)	# 产生指定范围的随机数
print random.choice([1, 5, 9, 0, 10, 13, 8])	# 在指定的序列中产生一个随机数
print random.sample([1, 2, 5, 8, 0, 10, 3, 6], 5)	# 在指定的序列中产生一个指定个数的不重复的序列


from time import *

date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
rt = random.uniform(time1, time2)
print rt
print asctime(localtime(rt))


from pprint import pprint

values = range(2, 11) + 'J Q K A'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
pprint(deck[:12])

random.shuffle(deck)
pprint(deck[:12])

count = len(deck)
while count > 0:
	print deck[count - 1]
	count -= 1