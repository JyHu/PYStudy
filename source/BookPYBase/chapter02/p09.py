#coding:utf-8

def zeroexc():
	try:
		print 1/0
	except ZeroDivisionError, e:	# 截取系统的异常对象
		print "The second number can't be zero"
		# raise	# 将异常往上提
		print 'System error info'
		print e

zeroexc()

class nzeroexc():
	muffled = True
	def calc(self):
		try:
			print '12' / 0
		except ZeroDivisionError:				# 多次接收异常
			if self.muffled:
				print 'Division by zero is illegal'
			else:
				raise
		except TypeError:
			if self.muffled:
				print 'Type error'
			else:
				raise

t = nzeroexc()
t.calc()


class dexc():
	def calc(self):
		try:
			print '12' / 0
		except (TypeError, ZeroDivisionError):		# 接收多个异常
			print 'error type and division number'
dexc().calc()

