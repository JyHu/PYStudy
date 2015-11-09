# 
# coding:utf-8
# 
# auth:JyHu
# 
# *** 生成器 generator ***
# 


# 把 [] 改成 () 即可生成一个generator
# generator 保存的是算法
# generator 每当next的时候才回去计算当前遍历到的数值
g = (x * x for x in range(10))
print(g)
print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())	# 到最后一个后，没有末尾元素了就会报错

for n in g:
	print(n)

def fib(num):
	n, a, b = 0, 0, 1
	while n < num:
		yield b
		a, b = b, a + b
		n = n + 1
	return

for i in fib(60):
	print i
