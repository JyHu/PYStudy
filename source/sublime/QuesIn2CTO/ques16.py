#coding:utf-8



'''

题目：输出指定格式的日期。

'''




import datetime

if __name__ == '__main__':
	print datetime.date.today().strftime('%d/%m/%Y')		# strftime 按格式化的格式来输出日期

	dateObj = datetime.date(1991, 1, 5)		# 创建一个日期对象
	print dateObj.strftime('%d-%m-%Y')

	dateObj = dateObj + datetime.timedelta(days = 1)	# 日期运算
	print dateObj.strftime('%d %m %Y')

	dateObj = dateObj.replace(year = dateObj.year + 1)	# 日期替换
	print dateObj.strftime('%d %m %Y')

def astest(num):
	assert 1 <= num <= 12, "assert number is %d" % num 	# 断言

astest(0)


# help(dateObj.strftime)
# help(datetime.timedelta)
# help(dateObj.replace)


# import datetime
 
# if __name__ == '__main__':
 
#     # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
#     print(datetime.date.today().strftime('%d/%m/%Y'))
 
#     # 创建日期对象
#     miyazakiBirthDate = datetime.date(1941, 1, 5)
 
#     print(miyazakiBirthDate.strftime('%d/%m/%Y'))
 
#     # 日期算术运算
#     miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
 
#     print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
 
#     # 日期替换
#     miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
 
#     print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))







'''



Help on class timedelta in module datetime:

class timedelta(__builtin__.object)
 |  Difference between two datetime values.
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __div__(...)
 |      x.__div__(y) <==> x/y
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __nonzero__(...)
 |      x.__nonzero__() <==> x != 0
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rdiv__(...)
 |      x.__rdiv__(y) <==> y/x
 |  
 |  __reduce__(...)
 |      __reduce__() -> (cls, state)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  total_seconds(...)
 |      Total seconds in the duration.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  days
 |      Number of days.
 |  
 |  microseconds
 |      Number of microseconds (>= 0 and less than 1 second).
 |  
 |  seconds
 |      Number of seconds (>= 0 and less than 1 day).
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 |  
 |  max = datetime.timedelta(999999999, 86399, 999999)
 |  
 |  min = datetime.timedelta(-999999999)
 |  
 |  resolution = datetime.timedelta(0, 0, 1)


'''