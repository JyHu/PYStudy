#coding:utf-8


def catcherror():
	while True:
		try:
			x = raw_input('Enter a number:')
			if int(x) < 10: print x
			else: print 1/0
		except:	# 如果try中又异常就会走到这里来，在这里捕捉到异常
			print 'Invalid input, please input again'
		else:	# 如果try中没有异常，走下来会走到这里
			break
		finally:	# 每次的try之后都会走到这里来
			print 'finally'

catcherror()


