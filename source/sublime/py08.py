#
# coding:utf-8
#
# auth:JyHu
# 

L = []
n = 1
while n <= 99:
	L.append(n)
	n = n + 2
print(L)

print('-----------------------------')

# List

S = list(range(100))

print(S)
print('-----------------------------')
print(S[:10])
print('-----------------------------')
print(S[-10:])
print('-----------------------------')
print(S[10:20])
print('-----------------------------')
print(S[:10:2])
print('-----------------------------')
print(S[::5])
print('-----------------------------')
print(S[:])
print('-----------------------------')

# Tuple
print((0, 1, 2, 3, 4, 5, 6, 7)[:3])

# String
print('ABCDEFGH'[1:6])