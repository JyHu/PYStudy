# 
# coding:utf-8
# 
# auth:JyHu
# 
# *** 杨辉三角 ***
# 


def yh(num):
	b = [1]
	while len(b) < num:
		yield b
		b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]

for i in yh(15):
	print i