
#coding:utf-8
#auther:jyhu

# list  tuple

#
# List
#

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(len(classmates))

for i in classmates:
	print('My name is %s ;' % i)

for i in range(len(classmates)):
	print('NO. %d name is %s' % (i, classmates[i]))

print(classmates[0])

print(classmates[-2])

classmates.insert(1, 'Jack')
print(classmates)

# 删除最后一个元素
print(classmates.pop())
#删除某个位置的元素
print(classmates.pop(1))

#list的元素可以不同
L = ['Apple', 123, True]
#list中的元素还可以也是list
s = ['python', 'Java', ['asp', 'php'],'scheme']





#
# Tuple 元组
#

# 跟list类似，不过，只要创建了就无法再修改
t = ('Michael', 'John', 'Tracy')
print(t)

#如果只有一个元素的话，则需要在后面加一个 ',' 来消除歧义
t = (1,)
print(t)





