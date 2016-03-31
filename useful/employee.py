#coding:utf-8
#auth:JyHu



'''

北京市税务局官网
http://gs.tax861.gov.cn/zxl.htm

1 不超过1500元的 3
2 超过1500元至4500元的部分 10
3 超过4500元至9000元的部分 20
4 超过9000元至35000元的部分 25
5 超过35000元至55000元的部分 30
6 超过55000元至80000元的部分 35
7 超过80000元的部分 45


养老		8%
医疗		%2
失业		%0.2
公积金	%12

'''

# 计算五险一金以及需要缴纳的个人所得税
# real_employee		实际税前工资
# IAHF_base			五险一金缴纳基础
# iahf 				五险一金缴纳的税率及比例
def insurance_and_housing_fund_count(real_employee, IAHF_base, iahf):

	# 五险一金总额
	insurance_and_housing_fund_count = (iahf["endowment_insurance_rate"] + iahf["medical_insurance_rate"] + 
										iahf["unemployment_insurance_rate"] + iahf["housing_fund_rate"]) * IAHF_base

	# 需要缴税的税前收入
	pre_tax_employee = real_employee - insurance_and_housing_fund_count - iahf["individual_income_tax_base"]

	# 需要缴纳的个人所得税总额
	individual_income_tax_count = 0.0

	iit_0_1500 		= 0.03 * 1500
	iit_1500_4500 	= 0.1  * (4500 - 1500)   + iit_0_1500
	iit_4500_9000 	= 0.2  * (9000 - 4500)   + iit_1500_4500
	iit_9000_35000 	= 0.25 * (35000 - 9000)  + iit_4500_9000
	iit_35000_55000 = 0.3  * (55000 - 35000) + iit_9000_35000
	iit_55000_80000 = 0.35 * (80000 - 55000) + iit_35000_55000


	if pre_tax_employee < 0 				: print "你不用交个人所得税"
	elif 0	   < pre_tax_employee <= 1500	: individual_income_tax_count = pre_tax_employee * 0.03
	elif 1500  < pre_tax_employee <= 4500 	: individual_income_tax_count = iit_0_1500 + (pre_tax_employee - 1500) * 0.1
	elif 4500  < pre_tax_employee <= 9000 	: individual_income_tax_count = iit_1500_4500 + (pre_tax_employee - 4500) * 0.2
	elif 9000  < pre_tax_employee <= 35000 	: individual_income_tax_count = iit_4500_9000 + (pre_tax_employee - 9000) * 0.25
	elif 35000 < pre_tax_employee <= 55000 	: individual_income_tax_count = iit_9000_35000 + (pre_tax_employee - 35000) * 0.3
	elif 55000 < pre_tax_employee <  80000 	: individual_income_tax_count = iit_35000_55000 + (pre_tax_employee - 55000) * 0.35
	else 									: individual_income_tax_count = iit_55000_80000 + (pre_tax_employee - 80000) * 0.45

	print "\n-------计算结果如下-------\n"

	print "养老保险     :", iahf["endowment_insurance_rate"] * IAHF_base
	print "医疗保险     :", iahf["medical_insurance_rate"] * IAHF_base
	print "失业保险     :", iahf["unemployment_insurance_rate"] * IAHF_base
	print "住房公积金   :", iahf["housing_fund_rate"] * IAHF_base
	print "个人所得税   :", individual_income_tax_count
	print "实际个人所得 :", real_employee - insurance_and_housing_fund_count - individual_income_tax_count

# 获取用户输入的一个数值
# prompt	提示文本
# def_num	用户输入值为0或者为空时的默认值
# not_zero	是否可以为0或为空
def effective_number(prompt, def_num, not_zero = False ):
	temp = raw_input(prompt)
	number = 0.0

	if not temp.strip(): number = 0.0
	else: number = float(temp)

	if not number > 0.0:	# 输入的数字为0
		if not_zero:
			print("输入无效，该字段不能为空，请重新输入。。。")
			return effective_number(prompt, not_zero)
		else: return def_num
	return number

# 判断是否为0
# num 		要判断的数字
# def_num	不合法时的默认值
def zero_judge(num, def_num):
	if num > 0.0: return num
	else: return def_num

# 数据录入并计算
def data_input():
	print "\n", "*" * 70, "\n", "*" * 70, "\n"

	emp  = effective_number("请输入税前工资(必须项，不能为空或0) : ", 0, True)
	iahf = effective_number("请输入五险一金缴纳基础(非必须项，默认以税前工资为基础) : ", 0)

	# 传得五险一金税率的参数
	t_iahf = {}

	# 如果输入的五险一金缴纳基础为0，那么就以输入的工资额为基础计算
	if not iahf > 0.0: iahf = emp

	t_iahf["individual_income_tax_base"]	= effective_number("请输入个人所得税缴纳基础(非必须项，默认以北京的3500为基础) : ", 3500)	# 个人所得税缴纳基础
	t_iahf["endowment_insurance_rate"] 		= effective_number("请输入养老保险税率(非必须项，默认以标准规定的0.08计算) : ", 0.08)		# 养老保险税率
	t_iahf["medical_insurance_rate"] 		= effective_number("请输入医疗保险税率(非必须项，默认以标准规定的0.02计算) : ", 0.02)		# 医疗保险税率
	t_iahf["unemployment_insurance_rate"] 	= effective_number("请输入失业保险税率(非必须项，默认以标准规定的0.002计算) : ", 0.002)	# 失业保险税率
	t_iahf["housing_fund_rate"] 			= effective_number("请输入住房公积金比例(非必须项，默认以标准规定的0.12计算) : ", 0.12)	# 住房公积金比例

	# 计算并显示结果
	insurance_and_housing_fund_count(emp, iahf, t_iahf)

	print "\n", "*" * 70, "\n", "*" * 70, "\n"

if __name__ == "__main__":
	while (1): data_input()







