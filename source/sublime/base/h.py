# 
# coding:utf-8
# 
# auth:JyHu
# 
# func:Function Help
# 


def showhelp(func):
	print('\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
	print(    ' * * * * * * * * * * * * * * Begin * * * * * * * * * * * * * *\n')
	print(func)

	help(func)

	print(    ' * * * * * * * * * * * * * * * End * * * * * * * * * * * * * *')
	print(    '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n')