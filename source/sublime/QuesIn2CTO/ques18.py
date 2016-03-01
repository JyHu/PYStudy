#coding:utf-8


'''

题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

'''





import math


def simSum(num, nums):
	assert ((nums < 0) or not isinstance(nums, (int, long)) or (num < 0) or not isinstance(num, (int ,long))), "错误的数据类型"
	# if (nums < 0) or not isinstance(nums, (int, long)) or (num < 0) or not isinstance(num, (int ,long)):
	# 	return 0
	count = 0
	for i in range(0, nums):
		for j in range(0, i + 1):
			count += int(math.pow(10, j)) * num
	return count

print simSum(3.3, 3)



