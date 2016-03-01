#coding:utf-8




import string
from math import pow


'''

此例显示了函数string.rjust()的用法，此函数可以把一个字符串放进指定宽度右对齐，左边用空格填充。类似函数还有string.ljust()和string.center()。这些函数不向外输出，只是返回转换后的字符串。如果输入字符串太长也不会被截断而是被原样返回。这样的处理可能会使你的列对齐失效，但这可能比截断要好一些，截断的结果是我们看到一个错误的值。（如果你确实需要截断的话总可以再加一层片断，如string.ljust(x,n)[0:n]）。 

'''


for x in range(1, 100):
	
	print '%-2d, %-4d, %-6d' % (x , pow(x, 2), pow(x, 3))
	# print string.rjust('x', 2), string.rjust('x * x', 3), string.rjust('x * x * x', 4)

help(string.rjust)