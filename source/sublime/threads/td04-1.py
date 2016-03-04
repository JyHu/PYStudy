#coding:utf-8

import threading
import time


class staticNum():
	def __init__(self):
		super(staticNum, self).__init__()
	knum = 10

class myThread(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
	def run(self):
		while staticNum.knum > 1:
			threadLock.acquire()
			staticNum.knum -= 1
			print 'Thread %s , counter = %d' % (self.name, staticNum.knum)
			time.sleep(1)
			threadLock.release()
			

threadLock = threading.Lock()


thread1 = myThread('Thread-1')
thread2 = myThread('Thread-2')

thread1.start()
thread2.run()

while not thread2.isAlive():
	print 'Thread-2 exit'
	break
