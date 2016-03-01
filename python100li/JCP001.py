#coding:utf-8

'''
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
　　　　　　掉不满足条件的排列。 
2.程序源代码：
'''

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                print i,j,k



'''
扩展一下，建立一个函数，计算从1到指定的最大值的三个不重复排列数的个数
'''
def differentNumberArrangeCount(maxnum, np):
	# 累计排列的个数
	count = 0
	for i in range(1, maxnum + 1):
		for j in range(1, maxnum + 1):
			for k in range(1, maxnum + 1):
				if (i != j) and (i != k) and (j != k):
					count += 1
					if np:
						print i, j, k
	return count
				


num = 100
print "from 1 to max number %d ,count : %d" % (num, differentNumberArrangeCount(num, False))








