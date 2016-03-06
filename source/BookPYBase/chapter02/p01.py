#coding:utf-8

import math

print math.pow(2, 3)
print 2 ** 3

print [None] * 10

mlist = [1, 2, 3, 4, 5, 6, 7, 8]
mlist.append(3)	# 在列表末尾追加数据
print mlist


print mlist.count(3)	# 计算列表中得某个元素的个数
print mlist.count(1)


tempList = [2, 4, 11]
mlist.extend(tempList)	# extend， 追加数据，修改了原有的列表
print mlist


print mlist.index(3)	# 获取元素在列表中得索引


mlist.insert(2, 'sec')	# 在指定的位置插入数据
mlist.insert(5, 'fif')
print mlist


print mlist.pop()	# 移除列表中得一个元素，默认移除最后一个元素，这是唯一的一个移除元素并可以返回数据的方法
print mlist
print mlist.pop(2)
print mlist


mlist.remove('fif')		# 移除列表中得某个元素
print mlist


mlist.reverse()	# 将数组翻转
print mlist


mlist.sort()
print mlist


