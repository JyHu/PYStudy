# 
# coding:utf-8
# 
# auth:JyHu
# 
# *** 列表生成式 ***
# 

L = [x * x for x in range(1, 11)]
print(L)

M = [x * x for x in range(1, 11) if x % 2 == 0]
print(M)

N = [m + n for m in 'ABC' for n in 'xyz']
print(N)

O = [m + n + o + p for m in 'ABC' for n in 'hig' for o in 'OPQ' for p in 'xyz']
print(O)

# 列出当前目录下的所有文件和目录名
import os
F = [d for d in os.listdir('.')]
print(F)

d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
for k, v in  d.items():
	print(k, '=', v)
K = [k + '=' + v for k, v in d.items()]
print(K)

W = ['Hello', 'World', 'IBM', 'Apple', 123, 7789, 'MicroSoft']
R = [x.lower() for x in W if isinstance(x, str)]
print(R)