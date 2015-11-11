# 
# coding:utf-8
# 

'''

'''

__author__ = 'JyHu'



# def foo(s):
# 	n = int(s)
# 	print('>>> n = %d' % n)
# 	return 10 / n

# def main():
# 	foo('0')

# main()





def foo(s):
	n = int(s)
	assert n != 0, 'n is zero !'
	return 10 / n

def main():
	foo('0')

main()

