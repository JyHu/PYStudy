#coding:utf-8





with open('write.txt', 'w') as f:
	f.write('line 1')
	f.write('line 2')
	f.write('line 3')

with open('write.txt') as f1:
	print f1.readlines()



with open('write.txt', 'w') as f2:
	f2.write('line 4')
	f2.write('line 5')

with open('write.txt') as f3:
	print f3.readlines()

with open('write.txt', 'a') as f4:
	f4.write('line 6')
	f4.write('line 7')
	# help(f4)
	pass

with open('write.txt') as f5:
	print f5.readlines()
