#coding:utf-8


'''
������5��
��Ŀ��������������x,y,z���������������С���������
1.���������������취����С�����ŵ�x�ϣ��Ƚ�x��y���бȽϣ����x>y��x��y��ֵ���н�����
������������Ȼ������x��z���бȽϣ����x>z��x��z��ֵ���н�����������ʹx��С��
2.����Դ���룺
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