#coding:utf-8


import json

data = ['k', 'b', 't', {'p' : 'e', 'f' : (3 ,0)}]
jstr = json.dumps(data)
djs = json.loads(jstr)

print 'data' + repr(data)
print 'encode' + jstr
print 'load' , djs
print djs[3]
print djs[3]['f']
print 'no sorted ' , jstr
print 'be sorted ' , json.dumps(data, sort_keys = True, indent = 2)
