# 
# coding:utf-8
# 

'''

大陆的身份证为18位，老的身份证是15位。 
关于身份证第18是怎么计算的，原理如下：根据〖中华人民共和国国家标准 GB 11643-1999〗中有关公民身份号码的规定，公民身份号码是特征组合码，由十七位数字本体码和一位数字校验码组成。排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位数字校验码。 
地址码（身份证前六位）表示编码对象常住户口所在县(市、旗、区)的行政区划代码。（所有区域的编码可以到这个网站http://www.stats.gov.cn/tjbz/index.htm 
查询到最新的县及县以上的行政编码资料。） 
生日期码（身份证第七位到第十四位）表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符。例如：1981年05月11日就用19810511表示。 
顺序码（身份证第十五位到十七位）为同一地址码所标识的区域范围内，对同年、月、日出生的人员编定的顺序号。其中第十七位奇数分给男性，偶数分给女性。 
校验码（身份证最后一位）是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。 

第十八位数字的计算方法为： 
1.将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 
2.将这17位数字和系数相乘的结果相加。 
3.用加出来和除以11，看余数是多少？ 
4余数只可能有0 1 2 3 4 5 6 7 8 9 10这11个数字。其分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。 
5.通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的Ⅹ。如果余数是10，身份证的最后一位号码就是2。 

例如：某男性的身份证号码是34052419800101001X。我们要看看这个身份证是不是合法的身份证。 
首先：我们得出，前17位的乘积和是189 
然后：用189除以11得出的结果是17 + 2/11，也就是说余数是2。 
最后：通过对应规则就可以知道余数2对应的数字是x。所以，这是一个合格的身份证号码。 

备注说明：关于大陆身份证有的人会发现前几位为什么变化了。这主要出现在中国的重庆。原有的重庆人的身份证多数以51开头。以前隶属于四川的原因。但新办的身份证可能是50开头，原因是行政区划改变所致。中国各地的行政区划代码请参考国家统计局网站http://www.stats.gov.cn/tjbz/index.htm 
参考资料：http://spaces.msn.com/members/kinworld 


411526  	地址码
1993  		年份
0716  		月日
810   		同一地区对同一日出生的孩子的编码，其中最后一位为奇数表示男，偶数为女
3			校验码



'''

__author__ = 'JyHu'



class Identify(object):
	def __init__(self, identity_card_id):
		pass













