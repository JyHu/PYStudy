#coding=utf-8

__author__ = 'JinyouHU'


'''
类的继承
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。

需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。

在python中继承中的一些特点：

1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

语法：

派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
'''


class Parent:
    parentAttr = 100
    def __init__(self):
        print 'Calling parent constructor'

    def parentMethod(self):
        print 'calling parent method'

    def printMethod(self):
        print 'Parent print method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print 'Parent attribute :',Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print 'calling child constructor'
    def childMethod(self):
        print 'calling child method'

print 1
c = Child()
print 2
c.childMethod()
print 3
c.parentMethod()
print 4
c.setAttr(200)
print 5
c.getAttr()
print 6



'''
重载方法
如果你的父类方法的功能不能满足你的需求，你可以在子类重载你父类的方法：
'''

print '\n\n\n重载方法\n'
class Child1(Parent):
    def parentMethod(self):
        print 'Child print method'

cd = Child1()
cd.printMethod()




'''
基础重载方法
下表列出了一些通用的功能，你可以在自己的类重写：

序号	方法, 描述 & 简单的调用
1	__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : dell obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
'''

print '\n\n基础重载方法\n'

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector(1, 2)

print v1 + v2 + v3


'''
隐藏数据
在python中实现数据隐藏很简单，不需要在前面加什么关键字，只要把类变量名或成员函数前面加两个下划线即可实现数据隐藏的功能，这样，对于类的实例来说，其变量名和成员函数是不能使用的，对于其类的继承类来说，也是隐藏的，这样，其继承类可以定义其一模一样的变量名或成员函数名，而不会引起命名冲突。 实例：
'''

print '\n\n隐藏数据\n'
class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.__secretCount