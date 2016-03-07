#coding:utf-8
# 集合

a = set([1, 2 ,3 ,4, 5])
b = set([2, 4 ,6, 8])
c = a & b
print a.union(b)
print a | b
print a.issubset(b)
print c
print c <= b
print c.issuperset(a)
print c >= a
print a.intersection(b)
print a.difference(b)
print a - b
print a.symmetric_difference(b)
print a ^ b
print a.copy()
print a.copy is a 

m = set()
n = set()
# m.add(n)
m.add(frozenset(b))	# frozenset用于代表不可变（可散列）的集合
print m