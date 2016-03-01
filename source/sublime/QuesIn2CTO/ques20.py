#coding:utf-8



'''

题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

'''


def halfCount(hight, num):
	msum = 0
	def tempFunc(tempHight, tempNum):
		if tempNum > 0 :
			msum += tempFunc(tempHight / 2.0, tempNum - 1) * 2 + tempHight
			return msum
		else:
			return 0
	return tempFunc(hight, num)

print halfCount(100, 3)






def halfCount1(hight, num):
	hig = hight
	nsum = hig
	for i in range(2, num + 1):
		hig /= 2.0
		nsum += hig * 2
	return nsum

print halfCount1(100, 10)



'''

time  count

1 		100
2		100 + 50 * 2
3		100 + 50 * 2 + 25 * 2

'''