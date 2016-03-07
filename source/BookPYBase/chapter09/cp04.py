#coding:utf-8



'''

任何包含yield语句的函数都称为生成器

当迭代器被调用时，在函数体中得代码不会被执行，而会返回一个迭代器；
每次请求一个值，就会执行生成器中的代码，直到遇到一个yield或者return语句

yield意味着应该生成一个值
return意味着生成器要停止执行

return语句只有在一个生成器中使用时才能进行无参数调用

'''



nested = [[1,2],[3,4],[5]]
def flatten(nes):
	for sublist in nes:
		for element in sublist:
			yield element
for num in flatten(nested):
	print num
print list(flatten(nested))


# 列表推导式	
g = ((i + 2) ** 2 for i in range(2, 27))
for num in g:
	print num
print 'sum ' + repr(sum(i ** 2 for i in range(2, 27)))




# 递归生成器

def flatten1(nes):
	try:
		try: nes + ''
		except TypeError: pass
		else: raise TypeError
		for sublist in nes:
			for element in flatten1(sublist):
				yield element
	except TypeError:
		yield nes
print list(flatten1([[[1], 2], 3, 4, [5, 6, [7, [8]]], 'a', 9]))


def flatten2(nes):
	try:
		try:nes + ''
		except: pass
		else: raise TypeError
		for sublist in nes:
			for element in flatten2(sublist):
				yield element
	except TypeError:
		yield nes

print list(flatten2([[[1], 2], 3, 4, [5, 6, [7, [8]]], 'a', 9]))






