
#coding:utf-8
#
# Dict & set
#
# Help(dict)  查看帮助
#


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 65
print(d)


# 判断是否存在这个 key
print('Thoms' in d)

# 可以使用dict的get方法来限制返回空值时的数据，这样也能避免取值非法的情况
p = d.get('Thoms', -1)
print(p)


#
#
#
# Set
# 
# 
# 


s = set([1, 2, 3, 3, 3])
print(s)

s.add(4)
s.remove(4)

s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])
print(s1&s2)

help(dict)