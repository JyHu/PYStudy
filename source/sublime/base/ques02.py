#
# coding:utf-8
# 
# auth:JyHu
# 


def charcount(str):
	counter = {}
	for c in str:
		if c in counter:
			counter[c] = counter[c] + 1
		else:
			counter[c] = 1

	maxer = []

	for (v) in counter:
		if maxer == []:
			maxer = [v]
		else:
			if counter[v] == counter[maxer[0]]:
				maxer.insert(0, v)
			elif counter[v] > counter[maxer[0]]:
				maxer = [v]
			else:
				pass


	return maxer, counter[maxer[0]]

print(charcount('Hello wor'))
print(charcount('Hello'))
print(charcount('afkasdfhkbnmbajhfadioiwefkasdnkfasmndcakjkasdkjal'))


# inputstr = input('Your String : ')
# print('your input string is : %s' % inputstr)
# print(charcount(String(inputstr)))