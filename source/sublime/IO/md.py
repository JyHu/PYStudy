# coding:utf-8




import md5

src = 'this is a md5 test.'   


m1 = md5.new()   
m1.update(src)   
print m1.hexdigest()   

import hashlib   

m2 = hashlib.md5()   
m2.update(src)   
print m2.hexdigest()  