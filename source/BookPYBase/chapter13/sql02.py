#coding:utf-8


import sqlite3


conn = sqlite3.connect('user.db')	# connect 返回连接对象
curs = conn.cursor()	# 通过游标来执行SQL查询并检查结果
try:	# 需要检查进行异常检查，因为如果存在数据表的话，再创建会产生异常
	curs.execute('''
		create table user(
		id int,
		name text,
		age int,
		phone text
	)
	''')
except Exception, e:
	print e
	pass
else:
	print 'create successed'
finally:
	pass

insert = 'insert into user values(?,?,?,?)'
for line in open('users.txt'):
	value = line.split(' ')
	curs.execute(insert, value)
conn.commit()	# 提交挂起的事物


query = 'select * from user where id=1'
print query
curs.execute(query)
names = [f[0] for f in curs.description]	# 获取每组的列名
print names
for row in curs.fetchall():
	for pair in zip(names, row):
		print '%s:%s' % pair




conn.close()	# 关闭数据库连接






'''


Date	日期
Time	时间
Timestamp	时间戳
DateFromTicks	自新纪元以来的秒数
TimeFromTicks	来自秒数的时间值
TimeStampFromTicks	来自秒数的时间戳值
Binary 		二进制字符串值
STRING		字符串
Binary		二进制列
NUMBER		数字
DATETIME 	日期/时间
ROWID		行ID


'''



