#coding=utf-8

__author__ = 'JinyouHU'

#define and invoke function

def sum(a,b):
    return a+b

func = sum      #

r = func(5,6)
print r

#defines functionwith default argument

def add(a,b=2):      #如果不给b赋值，会有一个默认的值
    return a+b
r = add(1)
print r
r = add(1,5)
print r


# the range() function

a = range(5, 10)
print a

a = range(-2, -7)
print a

a = range(-7, -2)
print a

a = range(-2, -11, -3)      #adding by step
print a


def printinfo(name,age=35):
    "print every string"
    print 'name ',name
    print 'age ',age

printinfo(age=50,name='miki')
printinfo('lucy',55)
printinfo('miky')



'''
加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
'''

def printUnSureFunc(arg1, *vartuple):
    "打印传入的参数"
    print 'output: '
    print arg1
    for var in vartuple:
        print var
printUnSureFunc(10)
printUnSureFunc(70, 60, 50, 40)
printUnSureFunc(100, {'name':'miki','age':24})





'''
匿名函数
用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。

Lambda函数能接收任何数量的参数但只能返回一个表达式的值，同时只能不能包含命令或多个表达式。
匿名函数不能直接调用print，因为lambda需要一个表达式。
lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda [arg1 [,arg2,.....argn]]:expression

'''
mysum = lambda arg1,arg2:arg1 + arg2
print 'value of total: ',mysum(10, 20)
print 'value of total: ',mysum(20, 20)