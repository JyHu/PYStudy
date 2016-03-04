#coding=utf-8

__author__ = 'JinyouHU'


print 'hello world'

# raw_input('Enter your name')
# raw_input('哈哈，输入中文')

a = 100
b = 201.1
c = 2343

print (a+b+c)/c


word = 'abcdefg'
a = word[2]

print 'a is : '+a

b = word[1:3]
print "b is :" +b

c = word[:2]
print 'c is :' +c

d = word[0:]
print 'd is :' +d

e = word[:2] + word[2:]
print 'e is :' +e

f = word[-1]
print 'f is :'+ f

g = word[-6:2]
print 'g is : ' +g

h = word[-2:]
print 'h is :' +h

i = word[:-2]
print 'i is :'+i

j = len(word)
print 'length of word is :' +str(j)

print 'input your Chinese name:'
s = raw_input('press enter to be continued')
print 'your name is :'+s
l = len(s)
print 'length of you Chinese name in asc codes is :' + str(l)
a = unichr(s)
l = len(a)
print "i'm sorry we should use unicode char! characters number of your chinese \
        name in unicode is:" + str(l)
