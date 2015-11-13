# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'

import json

def place_with_code(code):
	print('code : %s' % code)
	pcode = ''
	if isinstance(code, int):
		pcode = str(code)
	elif isinstance(code, str):
		pcode = code
	else:
		print('参数类型错误')
		return ()

	if len(pcode) == 6:
		with open('pcode.txt', 'r') as f:
			jstr = f.read()
			ej = json.loads(jstr, encoding = 'utf-8')
			v1 = ej['%s0000' % pcode[0:2]]
			v2 = ej['%s00' % pcode[0:4]]
			v3 = ej[pcode]

			return (v1, v2, v3)
	return ()

# print place_with_code('411526')
