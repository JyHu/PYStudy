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
	position = f3.tell()	# 查找当前位置
	if l == ' ':
		continue
	print(l)
f3.seek(0, 0) 	# 把指针再次重新定位到文件开头
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




'''

读文件的模式

r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

'''




'''

File对象的属性

file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

'''



