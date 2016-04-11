# coding:utf-8
# auth:JyHu


import os, time

file = 'test.txt'

def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st        #st导入的是os.stat file返回值
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev

st = os.stat(file)       #st导入的是os.stat file返回值

print "stat", file
dump(st)

fp = open(file)

st = os.fstat(fp.fileno())    #fp.fileno()获得文件描述符、 os.fstat(fp) 返回文件描述符fp的状态

print "fstat", file
dump(st)

