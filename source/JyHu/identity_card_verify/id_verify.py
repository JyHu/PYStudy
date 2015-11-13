# 
# coding:utf-8
# 

'''

校验码（身份证最后一位）是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。 

第十八位数字的计算方法为： 
1.将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 
2.将这17位数字和系数相乘的结果相加。 
3.用加出来和除以11，看余数是多少？ 
4余数只可能有0 1 2 3 4 5 6 7 8 9 10这11个数字。其分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。 
5.通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的Ⅹ。如果余数是10，身份证的最后一位号码就是2。 

http://www.stats.gov.cn/tjbz/index.htm 
参考资料：http://spaces.msn.com/members/kinworld 


411526  	地址码
1993  		年份
0716  		月日
810   		同一地区对同一日出生的孩子的编码，其中最后一位为奇数表示男，偶数为女
3			校验码



'''

__author__ = 'JyHu'

import place


# class Gender(Enum):
# 	Male = 0
# 	Female = 1


class Identify(object):
	def __init__(self, identity_card_id = ''):
		self._icid = identity_card_id
		try:
			if isinstance(identity_card_id, str):
				if len(identity_card_id) != 18 and len(identity_card_id) != 15:
					self._icid = ''
					raise TypeError('参数长度错误，不足18位或15位')					
			else:
				raise TypeError('参数类型错误，所提交的身份证号不是字符串')
		except TypeError as e:
			print(e)
		finally:
			pass

	def _code_verify_18(self):
		if not isinstance(self._icid, str):
			return False
		if len(self._icid) == 0:
			return False
		pcount = 0
		ratio = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
		for i in range(17):
			pcount = int(self._icid[i:i + 1]) * ratio[i] + pcount
		vcode = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')[pcount % 11]
		return vcode == self._icid[17:18].upper()

	# 私有方法，截取身份证号的一部分
	def _info_cut(self, b, l, d_str):
		if self.legitimate:
			return self._icid[b:b + l]
		else:
			return d_str

	# 身份证号码
	@property
	def identity_card_id(self):
		return self._icid

	# 简单判断是否合法，根据最后一位校验码
	@property
	def legitimate(self):
	    return self._code_verify_18()

	# 地区编码
	@property
	def place_code(self):
		return self._info_cut(0, 6, '******')

	# 出生日期
	@property
	def birth_year(self):
		return self._info_cut(6, 4, '****')

	# 出生月份
	@property
	def birth_month(self):
		return self._info_cut(10, 2, '**')

	# 出生日子
	@property
	def birth_day(self):
		return self._info_cut(12, 2, '**')

	# 性别
	@property
	def gender(self):
		g_code = int(self._info_cut(16, 1, '0'))
		return g_code % 2

	@property
	def area(self):
	    return place.place_with_code(self.place_code)
	
	def __str__(self):
		if self.legitimate:
			return ('%s %s-%s-%s' % (self.place_code, self.birth_year, self.birth_month, self.birth_day))
		else:
			return '非法身份证号'
	
if __name__ == '__main__':
	identity = Identify('41152619910828351')
	print(identity.place_code)
	print(identity.birth_year)
	print(identity.birth_month)
	print(identity.birth_day)
	print('gender', identity.gender)
	print(identity)
	print(identity.area)





