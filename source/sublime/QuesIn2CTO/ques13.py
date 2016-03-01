#coding:utf-8



'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''



from math import pow



for i in range(100, 1000):
	a = i % 10
	b = int(i/10)%10
	c = int(int(i/10)/10)%10
	if i == (pow(a, 3) + pow(b, 3) + pow(c, 3)) :
		print i


for i in range(1000, 10000):
	st = str(i)
	L = list(st)
	summ = 0
	for j in range(0, len(L)):
		n = int(L[j])
		summ += pow(n, 4)
		# print '%d - %d- %d - %d' % (i, n, pow(n, 3), summ)
	if summ == i:
		print i


# 扩展一下，可以计算类似的值，观察了一下规律，如果要3次方相加的话，必须是3位数，如果4次方的话，必须4位数，以此类推
# po：数字的位数
def perf(po):
	for num in range(int(pow(10, po - 1)), int(pow(10, po))):
		summ = 0
		for j in range(0, po):
			summ += pow(int(list(str(num))[j]), po)
		if summ == num:
			print num



perf(3)
perf(4)
perf(5)

