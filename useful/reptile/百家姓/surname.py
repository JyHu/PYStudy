# coding:utf-8
# auth:JyHu


from urllib import urlopen
import re
import sys
import os

# http://www.eywedu.com/baijiaxing/cy.asp?id=942

list_re = "<a\\s+href=\"(show.asp\\?id=[\\d]+?)\".*?>(.*?)</a>"
root_folder = "history_today"
errors_collect = []

# 抓取网页中的数据，并根据正则表达式返回匹配的结果
# page_url	页面地址
# re_pat	正则表达式

def load_web_page(page_url, re_pat):
	webpage = urlopen(page_url)
	text = webpage.read()
	syscode = sys.getfilesystemencoding()
	text = text.decode('gb2312', 'ignore').encode(syscode)
	return re.compile(re_pat).findall(text)

def make_folder(folder_path):
	try: os.mkdir(folder_path)
	except Exception, e: print e 

def save_surname(surname, filepath):
	sur_list = load_web_page("http://www.eywedu.com/baijiaxing/cyshow.asp?id=%s" % surname[0], "<td\\s+align=\"left\"\\s+bgcolor=#FFFFFF>([\\s\\S.]+?)</td>")
	text = sur_list[0].strip()
	text = re.sub(r'<(BR|br)>', '\n', text)	# 替换html中的br换行符
	text = re.sub(r'<.*?>', '', text)		# 替换穿插在法律内容中的html标签对
	text = re.sub(r'&nbsp;', '', text)		# 替换html中的空白字符
	if text and len(text) > 0:
		print "保存 %s 成功" % filepath
		with open(filepath, 'w') as f:
			f.write(text)
	else:
		print "\n\n"
		print "保存 %s 失败" % filepath

def load_surnames():
	make_folder("surname")
	for page in range(1, 6):
		sur_url = 'http://www.eywedu.com/baijiaxing/index.asp?page=%d&fl1=&fl2=' % page
		surname_list = load_web_page(sur_url, "<td\\s+width=10%><a\\s+href=javascript:cy\\('(\\d+?)'\\)>(.*?)</a></td>")
		for surname in surname_list:
			filepath = "surname/%s-%s.txt" % (surname[0], surname[1])
			try:
				if not os.path.exists(filepath):
					save_surname(surname, filepath)
				else:
					print "%s已经存在" % filepath
			except Exception, e:
				print e
				save_surname(surname, filepath)

if __name__ == "__main__":
	load_surnames()

