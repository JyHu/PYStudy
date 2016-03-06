#coding:utf-8



print 'Num string %010.4f' % 3.1415926	# 010表示这个数字转成字符串的时候有10位


tstring = 'Hello world, my name is Joyous'
print tstring.find('my')


from string import maketrans	
table = maketrans('ml', 'tt')	# 制作一个置换表，将字符串中的所有相应位置的'ml'字符替换为后面相应的'tt'
print tstring.translate(table)
print tstring
print tstring.translate(table, ' eus')	# 在替换的时候删除指定的字符


