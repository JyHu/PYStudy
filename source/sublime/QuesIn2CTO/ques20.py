#coding:utf-8



'''

题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

'''


# def halfCount(hight, num):
# 	if num == 1 : return hight
# 	def tempFunc(tempHight, tempNum):
# 		if tempNum ！= num :
# 			tempSum = tempFunc(tempHight / 2.0, tempNum - 1) * 2
# 			return tempSum
# 		return tempHight
# 	return tempFunc(hight, num)
# print halfCount(100, 3)





def jumpHight(height, num):
	jcount = 0
	def halfHeight(ht, nm):
		print "   -   " * 10
		if nm > 0:
			jcount += ht
			halfHeight(ht/2.0, nm-1)
		else: return
	halfHeight(height, num)
	return jcount
print jumpHight(100, 10)





def halfCount1(hight, num):
	hig = hight
	nsum = hig
	for i in range(2, num + 1):
		hig /= 2.0
		nsum += hig * 2
	return nsum
print halfCount1(100, 10)


from math import pow
def halfCount2(hight, num):
	nsum = hight
	for i in range(0, num): 
		if i != 0: nsum += hight * pow(1/2.0, i - 1)
	return nsum

print halfCount2(100, 10)



'''

time  count

1 		100
2		100 + 50 * 2
3		100 + 50 * 2 + 25 * 2

'''