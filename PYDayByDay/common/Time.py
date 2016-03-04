#coding=utf-8

__author__ = 'JinyouHU'

import time
import calendar

ticks = time.time()
print ticks


'''
什么是时间元组？
很多Python函数用一个元组装起来的9组数字处理时间:

序号	字段	值
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
上述也就是struct_time元组。这种结构具有如下属性：

序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''
localtime = time.localtime(time.time())
print 'local current time :\n',localtime
print localtime[0],localtime[1],localtime[3:6]


'''
获取格式化的时间
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
'''
localtime = time.asctime(time.localtime(time.time()))
print 'local current time :',localtime


cal = calendar.month(2008, 1)
print 'here is the calendar : '
print cal