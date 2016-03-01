# 
# coding:utf-8
# 
# auth:JyHu
# 
# *** 高阶函数 ***
# 


from h import showhelp


print('\n---------------------------\n Map Test\n')

# showhelp(map)


# 
# 
# Map
# 
# 接受两个参数，一个是函数，一个是 Iterator ，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回
# 
# 

print(abs(-10))
print(abs)

f = abs
print(f(-20))

abs = -10

def add (x, y, fun):
	return fun(x) + fun(y)
print(add(-5, -6, f))

    
'''

      /\
     /  \
     \   \
      \   \
  /\   \   \
 /  \   \   \
 \   \  /    \
  \   \/      \
   \      /\   \
    \    /  \  /
     \   \   \/
      \   \   
       \   \ 
        \  /
         \/

'''

# 将数字转换成字符

def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
print(r)
print(list(r))
print(list(map(str, [1,2,3,4,5,6,7,8])))



print('\n---------------------------\n Reduce Test\n')

# showhelp(reduce)

# 
# 
# Reduce
# 
# 作用：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 


# list中的元素乘积

from functools import reduce
def radd(x, y):
	return x * y
r = reduce(radd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)


# 将字符串转换成数字

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]
	return reduce(fn, map(char2num, s))

print(str2int('1234') * 2)






#
#
# Filter
# 
# 类似Map，不过是根据传入的参数来判断是否删除
# 
# 

print('\n---------------------------\n Filter Test\n')

# showhelp(filter)

# 去除偶数
# True 保留
# False 删除



# p = filter(lambda x : x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
p = filter(lambda x : x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(p)

# 
# 去除序列中的空字符串
# 
# s.strip(rm)	删除s字符串中开头、结尾处，位于rm删除序列的字符
# s.lstrip(rm)	删除s字符串中开头处，位于删除序列的字符
# s.rstrip(rm)	删除s字符串中结尾处，位于删除序列的字符
# 

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ''])))


print '=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-='
def madd(x, y):
	return x + y
print reduce(madd, range(101))




#
#
# Sorted
# 
# 排序
# 
# warning key排序属性没法使用
# 
# 

print('\n---------------------------\n Sourted Test\n')

showhelp(sorted)

print(sorted([36, -5, 1, 89, -7], key = abs))

