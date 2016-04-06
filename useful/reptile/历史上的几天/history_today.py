# coding:utf-8
# auth:JyHu

from urllib import urlopen
import re
import sys
import os


baseURL = 'http://ch.eywedu.com/today/'
list_re = "<a\\s+href=\"(show.asp\\?id=[\\d]+?)\".*?>(.*?)</a>"
detail_re = "<td><table.*?>([\\s\\S.]*?)</table></td>"
root_folder = "history_today"
errors_collect = []

# http://ch.eywedu.com/today/show.asp?id=4529

# http://ch.eywedu.com/today/index.asp?today=0427


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

def save_today_news(today_info, folder_path):
	detail_list = load_web_page("%s%s" % (baseURL, today_info[0]), detail_re)
	if len(detail_list) > 0:
		text = re.sub(r'<.*?>', '', detail_list[0])
		text = re.sub(r'(BR|br)', '\n', text)
		if len(text) > 0:
			with open(folder_path, 'w') as f:
				f.write(text)

		else:
			error_info = "\n\n", "*" * 70, "\n" "抓取到了空的内容", "\n", "地址是:", today_info[0], "\n", "名字是:", today_info[1], "*" * 70, "\n"
			errors_collect.append(error_info)
			print error_info

def collect_history_today_news():
	make_folder(root_folder)
	ht_count = 0
	for month in range(1, 13):
		make_folder("%s/%02d" % (root_folder, month))
		for day in range(1, 32):
			folder_name = "%s/%02d/%02d" % (root_folder, month, day)
			make_folder(folder_name)
			news_list = load_web_page("%sindex.asp?today=%02d%02d" % (baseURL, month, day), list_re)
			with open("history_today_log.txt", 'a') as f: 
				f.write("\n")
				f.write("*" * 60)
				f.write("\n%02d月%02d日\n" % (month, day))
				f.write("\n")
			if len(news_list) > 0:
				for today_new in news_list:
					jfilepath = "%s/%s.txt" % (folder_name, today_new[1].strip())
					try:
						if not os.path.exists(jfilepath):
							print "已经抓取到%04d条内容，正在抓取%02d月%02d日的内容：%s" % (ht_count, month, day, today_new[1])
							with open("history_today_log.txt", 'a') as f: f.write("%s\n" % today_new[1])
							save_today_news(today_new, jfilepath)
							ht_count = ht_count + 1
						else:
							print "%s 文件已经存在" % jfilepath
					except Exception, e:
						print e
			elif day > 28: break


if __name__ == "__main__":
	collect_history_today_news()
	if len(errors_collect) > 0:
		for er in errors_collect:
			print er






