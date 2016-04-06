# coding:utf-8
# auth:JyHu


import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(2)

threads = []
t1 = threading.Thread(target=music,args=('爱情买卖',))
# threads.append(t1)
t1.setDaemon(True)
t1.start()
t1.join()
t2 = threading.Thread(target=move,args=('阿凡达',))
t2.setDaemon(True)
t2.start()
t2.join()
sleep(1)
t3 = threading.Thread(target=music, args=('Thanks',))
t3.setDaemon(True)
t3.start()
t3.join()

# threads.append(t2)


if __name__ == '__main__':
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #     t.join()
    print "all over %s" %ctime()