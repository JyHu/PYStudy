#coding:utf-8

'''
������1��
��Ŀ����1��2��3��4�����֣�����ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
1.��������������ڰ�λ��ʮλ����λ�����ֶ���1��2��3��4��������е����к���ȥ
�����������������������������С� 
2.����Դ���룺
'''

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                print i,j,k



'''
��չһ�£�����һ�������������1��ָ�������ֵ���������ظ��������ĸ���
'''
def differentNumberArrangeCount(maxnum, np):
	# �ۼ����еĸ���
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








