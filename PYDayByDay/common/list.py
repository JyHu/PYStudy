#coding = utf-8

__author__ = 'JinyouHU'


word = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

a = word[2]
print 'a is :' +a

b = word[1:3]
print 'b is :'
print b

c = word[:2]
print 'c is :'
print c

d = word[0:]
print 'd is :'
print d

e = word[:2] + word[2:]
print 'e is :'
print e

f = word[-1]
print 'f is :'
print f

g = word[-4:2]
print 'g is :'
print g

h = word[-2:]
print 'h is :'
print h

i = word[:-2]
print 'i is :'
print i

l = len(word)
print 'length of word is :' + str(l)

print 'add new element...'
word.append('h')
print word

'''
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。

列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。

列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
'''


####################################################
'''
Python元组
元组是另一个数据类型，类似于List（列表）。

元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
'''


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素