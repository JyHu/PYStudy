#coding:utf-8




'''
������8��
��Ŀ�����9*9�ھ���
1.����������������п��ǣ���9��9�У�i�����У�j�����С�
2.����Դ���룺
#include "stdio.h"
main()
{
��int i,j,result;
��printf("\n");
��for (i=1;i<10;i++)
����{ for(j=1;j<10;j++)
��������{
����������result=i*j;
����������printf("%d*%d=%-3d",i,j,result);/*-3d��ʾ����룬ռ3λ*/
��������}
������printf("\n");/*ÿһ�к���*/
����}
}
'''
# for i in range(1,10):
#     for j in range(1,10):
#         result = i * j
#         print '%d * %d = % -3d' % (i,j,result)
#     print ''
    


'''

��ӡ��ʱ��

%3d��ʾ�Ҷ��룬ռ3λ
%-3d��ʾ����룬ռ3λ

'''


for i in range(1, 20):
	str = ""
	for j in range(1, i + 1):
		str += ("%2d*%-2d=%-3d " % (j, i, i * j))
	print "\n" + str






