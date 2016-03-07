#coding:utf-8



# shelve
# 是一个简单的存储解决方案


import shelve

s = shelve.open('test.dat', writeback = True)	# writeback 会在每次数据改变之后都存储一下
s['x'] = ['a', 'b', 'c']
s['x'].append('d')
print s['x']
s.close()



import sys

def store_person(db):
	'''
	Query user for data and store it in the shelf object
	'''

	pid = raw_input('Enter unique ID number:')
	person = {}
	person['name'] = raw_input('Enter name:')
	person['age'] = raw_input('Enter age:')
	person['phone'] = raw_input('Enter phone number:')

	db[pid] = person

def lookup_person(db):
	'''
	Query user for ID and desired field, and fetch the corresponding data from the shelf object
	'''

	pid = raw_input('Enter ID number:')
	field = raw_input('What whould you like to know?(name, age, phone?)')
	field = field.strip().lower()
	print field.capitalize() + ':' + db[pid][field]

def print_help():
	print 'the available commands are:'
	print 'store: stores information about a person'
	print 'lookup: looks up a person from ID number' 
	print 'quit: save changes and exit'
	print '? : prints this message'

def enter_command():
	cmd = raw_input('enter command (? for help)')
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open('database.bat')
	try:
		while True:
			cmd = enter_command()
			if cmd == 'store':
				store_person(database)
			elif cmd == 'lookup':
				lookup_person(database)
			elif cmd == '?':
				print_help()
			elif cmd == 'quit':
				return
	finally:
		database.close()

if __name__ == '__main__':
	main()


