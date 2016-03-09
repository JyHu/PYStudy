# coding:utf-8


import sqlite3


'''

标准数据库编程接口 https://www.python.org/dev/peps/pep-0249/	

python数据库编程指南 https://wiki.python.org/moin/DatabaseProgramming

'''


def convert(value):
	if value.startswith('~'):
		return value.strip('~')
	if not value:
		value = '0'
	return float(value)


conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()

curs.execute('''
	CREATE TABLE food(
	id 		TEXT 	PRIMARY KEY,
	desc	TEXT,
	water	FLOAT,
	kcal	FLOAT,
	protein	FLOAT,
	fat 	FLOAT,
	ash 	FLOAT,
	carbs 	FLOAT,
	fiber 	FLOAT,
	sugar 	FLOAT
	)
	''')

query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)'

for line in open('DATA_SRC.txt'):
	fields = line.split('^')
	print fields
	vals = [convert(f) for f in fields[:9]]
	curs.execute(query, vals)


conn.commit()
conn.close()



