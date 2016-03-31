# code:utf-8
# auth:JyHu


from urllib import urlopen
import re
import sys
import os


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

def save_surname():
	pass


def load_surnames():
	for page in range(1, 6):
		sur_url = 'http://www.eywedu.com/baijiaxing/index.asp?page=%d&fl1=&fl2=', page
		surname_list = load_web_page(sur_url, "<td\\s+width=10%><a\\s+href=javascript:cy\\('(\\d+?)'\\)>(.*?)</a></td>")


if __name__ == "__main__":
	load_surnames()

