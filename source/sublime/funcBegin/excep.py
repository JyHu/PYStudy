#coding:utf-8


import sys

for arg in sys.argv[0:]:
	try:
		f = open(arg, 'r')
		print 'open'
		print f.name
		print sys.argv
		print f.encoding
		print f.fileno
		print f.softspace
		print f.read()
		print '-=' * 40 
	except IOError:
		print "Can't open ", arg
		print '-=' * 40 
	else:
		print arg, '有', len(f.readlines()), '行'
		print '-=' * 40 
	finally:
		print 'finally'
		print '-=' * 40 
		f.close()

