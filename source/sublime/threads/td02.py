#coding:utf-8

import threading
import time

# class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
#     def __init__(self, num, interval):  
#         threading.Thread.__init__(self)  
#         self.thread_num = num  
#         self.interval = interval  
#         self.thread_stop = False  
   
#     def run(self): #Overwrite run() method, put what you want the thread do here  
#         while not self.thread_stop:  
#             print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())  
#             time.sleep(self.interval)  
#     def stop(self):  
#         self.thread_stop = True  
         
   
# def test():  
#     thread1 = timer(1, 1)  
#     thread2 = timer(2, 2)  
#     thread1.start()  
#     thread2.start()  
#     time.sleep(10)  
#     thread1.stop()  
#     thread2.stop()  
#     return  
   
# if __name__ == '__main__':  
#     test()  




'''

threading.Thread类的使用：
1，在自己的线程类的__init__里调用threading.Thread.__init__(self, name = threadname)
Threadname为线程的名字
2， run()，通常需要重写，编写代码实现做需要的功能。
3，getName()，获得线程对象名称
4，setName()，设置线程对象名称
5，start()，启动线程
6，jion([timeout])，等待另一线程结束后再运行。
7，setDaemon(bool)，设置子线程是否随主线程一起结束，必须在start()之前调用。默认为False。
8，isDaemon()，判断线程是否随主线程一起结束。
9，isAlive()，检查线程是否在运行中。

'''



class testThread(threading.Thread):
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.threadInterval = interval
        self.threadStop = False
    def tMethods(self):
        while not self.threadStop :
            print 'Thread %d , time:%s' % (self.threadNum, time.ctime())
            time.sleep(self.threadInterval)
    def run(self):
        self.tMethods()
    def stopThread(self):
        self.threadStop = True

def ttt():
    thd = testThread(1, 2)
    thd.start()
    time.sleep(10)
    thd.stopThread()

if __name__ == "__main__":
    ttt()