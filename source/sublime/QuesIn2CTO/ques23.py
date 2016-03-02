#coding:utf-8



'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''

class RhombusType:
	type1 = 1 << 0	# 样式1
	type2 = 1 << 1	# 样式2
	type3 = 1 << 2	# 样式3
	type4 = 1 << 3
	type5 = 1 << 4
	typeF = 1 << 8	# 添加外框，不能单独使用，必须跟前面的类型一起使用

# n : 字符的个数
# dc : 字符的样式
def doubleChar(n, dc = "*"):
	return dc * (2 * n + 1)

# n : 单向有多少层
# st : 整体距离左边边界多少个空格的距离
# type  菱形的类型
# fch : 菱形的字符的类型
def rhombus(n, st = 0, type = 0, fch = "*"):

	bstr = ' ' * st	 # 菱形整体距左边的距离空白字符
	estr = ''	# 如果有框的话作为菱形尾部的填充

	# 循环输出上半部分
	for i in range(0, n):
		if (type&RhombusType.typeF > 0):	# 需要外框
			estr = ' ' * (n - i) + fch
			if i == 0:	# 在第一行的时候，输出外框的头两行
				print ' ' * st + fch * (2 * (n + 1) + 1)
				print ' ' * st + fch + ' ' * (2 * n + 1) + fch
				bstr += fch

		if type & RhombusType.type1:	# 第一种菱形
			print bstr + ' ' * (n - i) + doubleChar(i, fch) + estr
		elif type & RhombusType.type2:	# 第二种菱形
			print bstr + ' ' * (n - i) + (fch + ' ') * (i + 1) + estr[1:]
		elif type & RhombusType.type3:	# 第三种菱形
			es = fch
			if i == 0:
				es = ' '
				estr = estr[1:]
			print bstr + ' ' * (n - i) + fch + doubleChar(i - 1, ' ') + es + estr

	# 循环输出下半部分
	for i in range(2, n + 1):
		if (type&RhombusType.typeF > 0):
			estr = ' ' * i + fch
		if type & RhombusType.type1:
			print bstr + ' ' * i + doubleChar(n - i, fch) + estr
		elif type & RhombusType.type2:
			print bstr + ' ' * i + (fch + ' ') * (n - i + 1) + estr[1:]
		elif type & RhombusType.type3:
			es = fch
			if i == n : es = ""
			print bstr + ' ' * i + fch + doubleChar(n - i - 1, " ") + es + estr

		if (type&RhombusType.typeF > 0) and (i == n):
			print ' ' * st + fch  + ' ' * (2 * n + 1) + fch
			print ' ' * st + fch * (2 * (n + 1) + 1)

def test(num = 2):
	rhombus(num, 10, RhombusType.type1)
	print('\n')
	rhombus(num, 10, RhombusType.type2)
	print('\n')
	rhombus(num, 10, RhombusType.type3)
	print('\n')
	rhombus(num, 10, RhombusType.type1|RhombusType.typeF)
	print('\n')
	rhombus(num, 10, RhombusType.type2|RhombusType.typeF)
	print('\n')
	rhombus(num, 10, RhombusType.type3|RhombusType.typeF)


test(5)



# num = 10
# for i in range(1, num + 1):
# 	rhombus(i, num - i, 2, ".")
# 	print ' ' * (num-i + 1) + doubleChar(i-1, "-")




'''

暂时输出一下六种类型


               *
              ***
             *****
            *******
           *********
            *******
             *****
              ***
               *


               * 
              * * 
             * * * 
            * * * * 
           * * * * * 
            * * * * 
             * * * 
              * * 
               * 


               * 
              * *
             *   *
            *     *
           *       *
            *     *
             *   *
              * *
               *


          *************
          *           *
          *     *     *
          *    ***    *
          *   *****   *
          *  *******  *
          * ********* *
          *  *******  *
          *   *****   *
          *    ***    *
          *     *     *
          *           *
          *************


          *************
          *           *
          *     *     *
          *    * *    *
          *   * * *   *
          *  * * * *  *
          * * * * * * *
          *  * * * *  *
          *   * * *   *
          *    * *    *
          *     *     *
          *           *
          *************


          *************
          *           *
          *     *     *
          *    * *    *
          *   *   *   *
          *  *     *  *
          * *       * *
          *  *     *  *
          *   *   *   *
          *    * *    *
          *     *     *
          *           *
          *************

'''