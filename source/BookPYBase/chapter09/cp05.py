#coding:utf-8



import sys, pprint, math
print pprint.pprint(sys.path)

args = sys.argv

import webbrowser
# webbrowser.open('http://www.baidu.com')


import fileinput
for line in fileinput.input(inplace = True):
	line = line.rstrip()
	num = fileinput.lineno()
	print '%-60s # %2i' % (line, num)