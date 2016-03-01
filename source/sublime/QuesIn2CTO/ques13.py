#coding:utf-8



'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''



from math import pow
import thread
import threading



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
	if summ == i:
		print i


class perf_number(threading.Thread):
	def __init__(self, po):
		threading.Thread.__init__(self)
		self.po = po

	def run(self):
		self.perf(self.po)

	def perf(po):
		print po
		for num in range(int(pow(10, po - 1)), int(pow(10, po))):
			summ = 0
			for j in range(0, po):
				summ += pow(int(list(str(num))[j]), po)
			if summ == num:
				print num

perf_number(6).start()

# perf(3)
# perf(4)
# perf(5)
# perf(6)







