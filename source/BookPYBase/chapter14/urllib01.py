#coding:utf-8


'''


urllib	简单的下载
urllib2	需要使用http验证或cookie，或者为自己的协议编写扩展程序

'''

from urllib import urlopen

webpage = urlopen('http://www.yw11.com/namelist.php')
print webpage
# print webpage.read()


import re

text = webpage.read()
# print text
pat = re.compile('http:.*?"')
for p in pat.findall(text):
	print p


