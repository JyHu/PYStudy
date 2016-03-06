#coding:utf-8

import threading
import time


class staticNum():
	def __init__(self):
		super(staticNum, self).__init__()
	counter = 0

class myThread(threading.Thread):
	def __init__(self):
		super(myThread, self).__init__()

	def run(self):
		staticNum.counter += 1









