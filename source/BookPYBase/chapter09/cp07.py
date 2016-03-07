#coding:utf-8
#堆


print '\n'
print '#' * 60
print '堆 heap'
print '#' * 60
print '\n'

from heapq import *
from random import shuffle

data = range(10)
shuffle(data)	#打乱数据
heap = []
for n in data:
	heappush(heap, n)	# 将数据推入堆中
print heap
heappush(heap, 0.5)
print heap
print heappop(heap)		# 推出堆中得最小的值
print heappop(heap)
print heappop(heap)
print heappop(heap)
print heappop(heap)
print heap




heap1 = [4 ,1, 0 ,9 ,7, 5]
heapify(heap1)	# 如果之前的堆在创建的时候没有使用push，需要在使用之前用heapify转为合法的堆
print heap1
heapreplace(heap1, 5)	# 推出堆中最小的值并推入一个新的值
print heap1



print '\n'
print '#' * 60
print '双端队列 deque'
print '#' * 60
print '\n'

##################################################################
# 双端队列


from collections import deque
q = deque(range(5))		# 创建一个双端队列
q.append(5)	# 在队列末尾追加一个数据
q.appendleft(6)	# 在队列的左边追加一个数据
print q
print q.pop()	# 将队列的末尾的数据推出并返回
print q
print q.popleft()	# 将队列左边的数据推出并返回
print q
q.rotate()	# 将队列左后一个移到前面来，相当于整体往右移	
print q
q.rotate()
print q




print '\n'
print '#' * 60
print '时间 time'
print '#' * 60
print '\n'

import time

'''

python 日期元组的字段含义

0	年		
1	月			0 ~ 12
2	日 			0 ~ 31
3	时 			0 ~ 23
4	分 			0 ~ 59
5	秒	 		0 ~ 61	为了应付闰秒和双闰秒
6	周			0 ~ 6 (周一 ~ 周日)
7	儒历日 		1 ~ 366
8	夏令时 		0、1、-1

'''

print time.asctime()
print time.localtime(1435358882)
# help(time)




