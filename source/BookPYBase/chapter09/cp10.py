#coding:utf-8
# re python中得正则表达式


import re

pat = re.compile('\\d')	# 用给定的正则字符串创建一个正则对象
print pat.search('87asd98fa9s7d9fad9as7d098f70a')	# search，找到返回MatchObject对象，否则返回None

st = 'alpha, beta, ,,,, gamma delta'
print re.split('[, ]+', st)
print re.split('[, ]+', st, maxsplit = 2)	# 用给定的正则来分割要处理的字符串
print re.split('[, ]+', st, maxsplit = 1)	# maxsplit设定的是能被分割的最大的次数



pchar = '[a-zA-Z]+'
text = 'asdf 33498a8sdf" asdf,;.jsaldf"asdf 080as8d as8d f0as8d'
ppat = re.compile(pchar)
print ppat.findall(text)	# 匹配给定字符串中所有符合要求的结果




rpat = '{name}'
rtext = 'Dear {name}， {name}'
print re.sub(rpat, 'Mr. Gumby', rtext)	# 用给定的字符串来替换正则匹配出来的结果


print re.escape('www.python.org')	# 将字符串中所有能被理解为正则表达式的子字符串都替换掉
print re.escape('But where is the hourse?')



m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print m.group(1)	# 获取正则匹配的某个组
print m.start(1)	# 获取正则匹配的某个组字符串在整个字串中得起始位置
print m.end(1)		# ……………………结束位置
print m.span(1)		# 起始位置和结束位置，(b,e)



emphasis_pattern = r'\*([^\*]+)\*'
# 使用VERBOSE标识，可以更清楚的说明正则表达式，让别人更容易看懂
emphasis_pattern = re.compile(r'''
			\*		# beginning emphasis tag -- an asterisk
			(		# begin group for capturing phrase
			[^\*]+	# capture anything except asterisks
			)		# end group
			\*		# ending emphasis tag
	''', re.VERBOSE)
print re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')	# 使用到了匹配组
