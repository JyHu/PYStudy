#coding:utf-8


'''

比较费解的exec和eval

'''



exec "print 'hello world'"

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()
# print scope.values()


exec 'print 1 + 5 * 9 / 3.4'

eval(raw_input('Enter an arithmetic expression : '))

