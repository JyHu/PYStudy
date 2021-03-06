#coding:utf-8

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.delay = delay
	def run(self):
		print 'Starting ' + self.name
		print_time(self.name, self.delay, 5)
		print 'Exiting ' + self.name
def print_time(threadName, delay, counter):
	while  counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print '%s : %s' % (threadName, time.ctime(time.time()))
		counter -= 1



thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

thread1.start()
thread2.run()



while thread2.isAlive():
	if not thread1.isAlive():
		exitFlag = 1
print 'Exiting main thread'