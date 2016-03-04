#coding:utf-8



import thread
import time
import threading

def print_time(threaname, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print '%s:%s' % (threaname, time.ctime(time.time()))

try:
	thread.start_new_thread(print_time, ('thread-1', 2, ))
	thread.start_new_thread(print_time, ('thread-2', 3, ))
except Exception, e:
	print e
else:
	print 'else'
finally:
	print 'finally'



print threading.enumerate()



