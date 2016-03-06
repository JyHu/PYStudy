#coding:utf-8

d = {}
d['name'] = 'Micky'
d['age'] = 35
print d

y = d.copy()
y['name'] = 'Chain'
print y
print d


from copy import deepcopy
dc = deepcopy(d)
dc['name'] = 'Jane'
print dc
print d



fd = {}.fromkeys(d)	# 取出字典中的所有的键，value为默认的none
print fd
fd2 = {}.fromkeys(d, 'default')	# 定义默认的value
print fd2


# print d['from']	#如果没有这个键的时候会崩溃，这时候需要
print d.get('from')
print d.get('from', 'Default get value')	# 如果没有这个键的话，返回默认的值



print d.has_key('name')	#判断有没有这个键


print d.items()	# 将字典中所有的数据取出返回一个列表
print d.iteritems()	# 返回一个迭代器


print d.keys()	# 所有的key，不会有重复的
print d.iterkeys()

print d.values()	# 所有的value，会有重复的
print d.itervalues()


d['from'] = 'henan'
d['employee'] = 'coder'
d['sex'] = 'male'
d['height'] = 168
d['weight'] = 54
print d.pop('name')	# 删除指定的键值对，并返回value
print d
print d.popitem()	# 随机删除一个键值对，并返回被删除的键值对
print d



dd = {}
dd.setdefault('name', 'N/A')
print dd
dd['name'] = 'Micky'
print dd
dd.setdefault('name', 'N/A')	# 设置一个默认的值，如果键对应的有值，则返回有效的值，如果没有的话返回设置好的默认的值
print dd



d1 = {
		'title': 'local title',
		'url' : 'http://www.localpython.com',
		'changed':'Mar 14'
		}
d2 = {'title' : 'remote title', 'changed' : 'Jan 08'}
d1.update(d2)	# 用后面的d2的来更新d1相对应key的值
print d1














