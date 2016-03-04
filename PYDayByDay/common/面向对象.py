#coding=utf-8

__author__ = 'JinyouHU'

class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print 'Total Tmployee %d' % Employee.empCount

    def displayEmployee(self):
        print 'name : ',self.name, ', Salary: ',self.salary


'This  would create first object of employee class'
emp1 = Employee('Zara', 2000)
print 'current Employee %d' % Employee.empCount     #相当于一个类的静态变量，对所有的实例化对象通用
'This would create second object of Employee class'
emp2 = Employee('Manni', 5000)


emp1.displayEmployee()
emp2.displayEmployee()

print 'total employee %d' % emp1.empCount

#实例化的对象也能动态的添加属性，但是只能是给自己添加并不会作用在其他的已经实例化或者即将实例化的对象上
emp1.age = 7
print  emp1.age

#       使用内联函数操作一个实例化对象
# print hasattr(emp1, 'age')
# print getattr(emp1, 'age')
# setattr(emp1, 'age', 8)
# delattr(emp1, 'age')

print emp1.age

emp1.age = 19
print emp1.age

del emp1.age
# print emp1.age   # un safe


'''
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
Python内置类属性调用实例如下：
'''

print '\n\n\npy 的内置属性，如下\n'
print 'Employee.__doc__:', Employee.__doc__
print 'Employee.__name__:', Employee.__name__
print 'Employee.__module__:', Employee.__module__
print 'Employee.__bases__:', Employee.__bases__
print 'Employee.__dict__:', Employee.__dict__


'''
Py的垃圾回收机制
采用的是OC中的计数器加减法类似的方式
'''

print '\n\npy的垃圾回收机制\n'
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, 'destroyed'

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3)  #打印对象的id
del pt1
del pt2
del pt3
