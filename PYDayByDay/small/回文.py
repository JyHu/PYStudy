#coding=utf-8

import math
from pip._vendor.distlib.compat import raw_input
import common

__author__ = 'JinyouHU'


#
# content = dir(common)
# print content

s = raw_input('判断回文字符串')
print (s == s[::-1])


while s!=s[::-1]:
    print ('False')
    s = raw_input('')
print ('True')



