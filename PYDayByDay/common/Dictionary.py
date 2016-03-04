#coding=utf-8

__author__ = 'JinyouHU'


'''
Python元字典
字典(dictionary)是除列表意外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
'''


dict = {}
dict['one'] = 'this is first'
dict[2] = 'this is second'

tinyDict = {'name':'john','code':6734,'dept':'sales'}

print dict['one']
print dict[2]
print tinyDict['name']
tinyDict['name']='haha'
print tinyDict['name']
print tinyDict
print tinyDict.keys()
print tinyDict.values()

del dict['code']    #删除一个元素
dict.clear()        #清空