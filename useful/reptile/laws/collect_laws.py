# coding:utf-8
# auth:JyHu


from urllib import urlopen
import re
import sys
import os

baseURL = "http://ds.eywedu.com/law/"

# 法律地址的数据源
urls = 	{
			# "xf" : "宪法",
			# "xingfa" : "刑法",
			"msf" : "民商法",
			"ssf" : "诉讼法",
			# "xzf" : "行政法"
		}

# 抓取网页中的数据，并根据正则表达式返回匹配的结果
# page_url	页面地址
# re_pat	正则表达式
def load_web_page(page_url, re_pat):
	webpage = urlopen(page_url)
	text = webpage.read()
	syscode = sys.getfilesystemencoding()
	text = text.decode('gb2312', 'ignore').encode(syscode)
	return re.compile(re_pat).findall(text)

# 抓取法律的具体内容
# law_url	法律地址
# law_name	法律的名字，包含了上级目录
def catch_law_detail(law_url, law_name):
	res = load_web_page(law_url, "<(FONT|font)\\s+class=.*?id=zoom>([\\s\\S.]*?)</font>")
	if len(res) >= 1 and len(res[0]) >= 2:
		text = res[0][1]	# 取第一个分组中抓取到的具体内容
		text = re.sub(r'<(BR|br)>', '\n', text)	# 替换html中的br换行符
		text = re.sub(r'<.*?>', '', text)		# 替换穿插在法律内容中的html标签对
		text = re.sub(r'&nbsp;', '', text)		# 替换html中的空白字符
		if len(text.strip()) > 0:		# 去掉空白字符，然后判断是否有效
			with open(law_name, 'w') as f:
				f.write(text)			# 写入到具体目录中
		else: 
			print "\n\n", "*" * 70, "\n" "抓取到了空的内容", "\n", "地址是:", law_url, "*" * 70, "\n"
	else:
		print "\n\n", "*" * 70, "\n" "抓取到了空的内容", "\n", "地址是:", law_url, "\n", "*" * 70, "\n"

def collect_pages():

	# 总共抓取到的法律数量
	total_count = 0

	for law,folderName in urls.items():
		try: os.mkdir(folderName)	# 创建一个法律的目录
		except Exception, e: print e

		page = 1		# 如果有下一页的话，累加去抓取下一页的内容
		cur_count = 1
		cur_total = 0

		while True:
			# 抓取网页中法律的列表
			law_list = load_web_page("%s%s/%s%d.htm" % (baseURL, law, law, page), "<a\\s+href=(\\d.*?)>(.*?)</a>")
			cur_total = cur_total + len(law_list)

			if len(law_list) > 0: 		# 如果抓取到的法律列表有内容，就抓取每部法律下的具体内容
				for res in law_list:	# 遍历去抓取具体内容
					print "已抓取到[%03d]部法律内容，正在抓取 《%s》 中的第[%03d/%03d]部法律 《%s》 的内容" % (total_count, folderName, cur_count, cur_total, res[1].strip())
					catch_law_detail("%s/%s/%s" % (baseURL, law, res[0]), "%s/%d-%s.txt" % (folderName, cur_count, res[1].strip()))
					total_count = total_count + 1
					cur_count = cur_count + 1
			else : break	# 没有内容就跳出去，然后继续抓下一种类型的法律
			page = page + 1

if __name__ == "__main__":
	collect_pages()
	# catch_law_detail("http://ds.eywedu.com/law/xf/200802/20080204101227.htm", "test.txt")


