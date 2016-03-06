#coding:utf-8


from math import sqrt as foobar	# 使用as将import的函数重命名，避免import的函数有重复的

print foobar(4)

age = 4
assert 0 < age < 100
# assert 10 < age < 100, 'error age'

zname = ['Micky', 'Jane', 'John', 'Ann']
zage = [18, 21, 9, 22]
for name, age in zip(zname, zage):	# zip可以将两个序列合并在一起，合并按少的来
	print name, age

for index, name in enumerate(zname):	# 枚举
	print index, name


f1 = [x * x for x in range(10)]
print f1
f2 = [x * x for x in range(20) if x % 3 == 0]
print f2
f3 = [(x, y) for x in range(3) for y in range(4)]
print f3
f4 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(20) if y % 3 == 0]
print f4
f5 = [x + y + x * y for x in range(10) if x % 2 == 0 for y in range(20) if y % 3 == 0]
print f5
