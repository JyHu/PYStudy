#coding:utf-8


'''

列表

列表数据类型还有其它一些方法。下面是列表对象的所有方法：  

insert(i, x) ---- 在指定位置插入一项。第一自变量是要在哪一个元素前面插入，用下标表示。例如，a.insert(0, x)在列表前面插入，a.insert(len(a), x)等价于a.append(x) 。  
append(x) ---- 等价于a.insert(len(a), x)  
index(x) ---- 在列表中查找值x然后返回第一个值为x的元素的下标。没有找到时出错。  
remove(x) ---- 从列表中删去第一个值为x的元素，找不到时出错。  
sort() ---- 对列表元素在原位排序。注意这个方法改变列表，而不是返回排序后的列表。  
reverse() ---- 把列表元素反序。改变列表。  
count(x) ---- 返回x在列表中出现的次数。 

'''


a = [66.6, -1, 333, 1, 1234.5, 333] 
print a.count(333), a.count(66.6), a.count('x')
print a.index(333)

a.reverse()
print a

a.sort()
print a

a.sort(reverse=True)
print a

help(a.sort)



del a[0]
print a

del a[-1]
print a



print 1 < 2 < 3 == 4


print (1, 2, 3) < (1, 2, 2)
print 'ABC' < 'C' < 'Pascal' == 'Python'
print (1, 2, ('aa', 'bb')) < (1, 2, 3, 4)




def fib(x):
	f = []
	a, b = 0, 1
	while b < x:
		f.append(b)
		a, b = b, a + b
	return f
print fib(1000)





