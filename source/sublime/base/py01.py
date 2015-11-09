
#coding:utf-8

#要想在python注释中添加中文的话，必须在第一行或者第二行添加 #coding:utf-8

print('hello, world')

a = 123
print(a)

a = 'abc'
print(a)

# 取得字符的ASCII码
print(ord('a'))
# 将ASCII码转成对应的字符
print(chr(66))

print('ABC'.encode('ascii'))

print(b'ABCD'.decode('ascii'))

print(len('ABCDEFGHI'))

print('Hello, %s' % 'world')

print('Hi, %s , you have $%s' % ('Michael', 10000))

print('%3d ~ %03d' % (2, 6))

print('%06.2f' % 3.14159)