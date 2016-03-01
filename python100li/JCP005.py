#coding:utf-8


'''
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
2.程序源代码：
'''
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l




'''
=========================================================================
'''


def rankArr1(ar):
	newArr = ar
	for i in range(len(newArr) - 1):
		for j in range(i + 1, len(newArr)):
			if newArr[i] > newArr[j]:
				temp = newArr[j]
				newArr[j] = newArr[i]
				newArr[i] = temp

	return newArr


# arr = []
# for j in range(3):
# 	n = int(raw_input('integer: '))
# 	arr.append(n)
# arr.sort()
# print(arr)



nar = []
for k in range(5):
	n = int(raw_input("integer : "))
	nar.append(n)

print rankArr1(nar)