# 
# coding:utf-8
# 

'''
基础I/O
'''

__author__ = 'JyHu'


print('------------------------------------------- 01')



try:
	f = open('test.txt', 'r') 	# 打开一个文件流，'r' 表示读
	print(f.read())		# 读取一个文件流的内容
finally:
	if f:
		f.close() 	# 关闭文件，每次打开必须关闭


print('------------------------------------------- 02')


# python 中有 with 语法可以自动的帮我们调用 close() 方法。
# 上面的相当于

with open('test.txt', 'r') as f1:
	print(f1.read())


print('------------------------------------------- 03')


# 读取一定字节数的内容

f2 = open('test.txt', 'r')
print(f2.read(10))
f2.close()



print('------------------------------------------- 04')



# 读取一行

f3 = open('test.txt', 'r')
while True:
	l = f3.readline()
	if l == '':
		break
	print(l)
f3.close()



print('------------------------------------------- 05')



# 读取多行，返回的是一个 list

f4 = open('test.txt', 'r')
for line in f4.readlines():
	print(line.strip())
f4.close()



print('------------------------------------------- 06')



# 读取二进制文件，比如文件

f5 = open('t.png', 'rb')
print(f5.read())
f5.close()




# encoding 文件的编码格式
# errors 忽略编码错误问题
# 
# with open('test.txt', 'r', encoding = 'gbk', errors = 'ignore') as f6:
# 	print(f6.read())



print('------------------------------------------- 07')


# 写文件
# 也能传入 encoding 参数设置写到的文件的编码格式

with open('write.txt', 'w') as f7:
	f7.write('write text test')
with open('write.txt', 'r') as f8:
	print(f8.read())










