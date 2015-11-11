# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'



def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass



try:
	print('try ...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally')
print('END')



print('\n')



try:
	print('try ...')
	r = 10 / int('a')
	print('result: ', r)
except ValueError as e:
	print('ValueError: ', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError: ', e)
finally:
	print('finally')
print('END')




print('\n')




# try:
# 	foo()
# except ValueError as e:
# 	print('ValueError ....')
# except UnicodeError as e:
# 	print('UnicodeError')





import logging

def foo1(s):
	return 10 / int(s)

def bar1(s):
	return foo1(s) * 2

def main():
	try:
		bar1('0')
	except Exception as e:
		logging.exception(e) 	# 通过记录错误log，当出错的时候会抛出错误，但是还会继续运行

main()
print('END')























