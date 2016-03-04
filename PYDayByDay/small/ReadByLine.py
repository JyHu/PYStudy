#coding=utf-8

__author__ = 'JinyouHU'


file = open("fz.txt")
while 1:
    line = file.readline()
    if not line:
        break
    print(line)
