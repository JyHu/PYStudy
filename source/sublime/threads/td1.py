#!/usr/bin/python 
# -*- coding: UTF-8 -*- 




import time  
import thread  
import sys

def timer(no, interval):  
	print 'timer'
    cnt = 0  
    while cnt<10:  
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt += 1  
    thread.exit_thread()  
     
   
def test(): #Use thread.start_new_thread() to create 2 new threads  
    thread.start_new_thread(timer, (1,1))  
    thread.start_new_thread(timer, (2,2))  
   
if __name__=='__main__':  
    test()
