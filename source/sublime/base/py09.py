# 
# coding:utf-8
# 
# auth:JyHu
# 

d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
for key in d :
	print(key, d[key])

for ch in 'ABCDEFG':
	print(ch)
#
# collections模块
# 
from collections import Iterable
print(isinstance('abc', Iterable)) 	# 判断是否是可迭代对象
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
for i, value in enumerate('ABCDEFG'):
	print(i, value)