#coding=utf-8

__author__ = 'JinyouHU'


spath = '/Users/k/Desktop/test.txt'
f = open(spath, 'w')
f.write('写入中文.\n')
f.writelines('中文一行.')

f.close()

f = open(spath,'r')

for line in f:
    print line

f.close()