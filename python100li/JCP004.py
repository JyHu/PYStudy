#coding:utf-8


'''题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.程序源代码：
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum









def leapYear(y):
	return (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))

def daysCount(y, m, d):
	md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if leapYear(y):
		md[2] = 29
	count = 0
	for i in range(1, m):
		count += md[i]

	return count + d

print "days count %d day" % daysCount(year, month, day)
