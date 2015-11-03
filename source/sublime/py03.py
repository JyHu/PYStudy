
#coding:utf-8
#
#
#
#
# # # # # # # # # # # # # # # # # # 
#
# 	   warning - 需要在终端运行
# 
# # # # # # # # # # # # # # # # # #
# 
# 
# 

age = 3

if age >= 18:
	print('adult')
elif age > 6:
	print('tennager')
else:
	print('kid')



inWeight = input('请输入你的体重(kg)：')
inHeight = input('请输入你的身高(cm)：')

weight = float(inWeight)
height = float(inHeight)

bmi = weight / (height / 100.0 * height / 100.0)

print('你的BMI指数为：%.2f' % bmi)

if bmi > 32:
	print('严重肥胖')
elif bmi > 28:
	print('肥胖')
elif bmi > 25:
	print('过重')
elif bmi > 18.5:
	print('正常')
else:
	print('过轻')