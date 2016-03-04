#coding=utf-8

__author__ = 'JinyouHU'


import thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s : %s' % (threadName, time.ctime(time.time()))


'''
注意方法名，参数的传递方法
'''

try:
    thread.start_new_thread(print_time, ('Thread-1', 2))
    thread.start_new_thread(print_time, ('Thread-2', 3))
except:
    print 'Error : unable to start thread'


while 1:
    pass