# coding:utf-8
# auth:JyHu

from urllib import urlopen
import re
import sys
import os


# http://ch.eywedu.com/36/index.html
# http://ch.eywedu.com/36/01.htm


def load_web_page(page_url, re_pat):
	webpage = urlopen(page_url)
	text = webpage.read()
	syscode = sys.getfilesystemencoding()
	text = text.decode('gb2312', 'ignore').encode(syscode)
	return re.compile(re_pat).findall(text)

def make_folder(folder_path):
	try: os.mkdir(folder_path)
	except Exception, e: print e 

def save_36stratagem():
	make_folder('36stratagem')
	stratagemlist = load_web_page('http://ch.eywedu.com/36/index.html', '第(\\d+)计\\s+<a\\s+target.*?href=\"(.*?)\">.*?>(.*?)</font></a>')
	for stratagem in stratagemlist:
		detaillist = load_web_page('http://ch.eywedu.com/36/%s' % stratagem[1], '<td\\s+bgcolor=\"#EEECFF\"\\s+class=\"p141\">\\s+<.*?>([\\s\\S.]*?)</font></td>')
		text = detaillist[0].strip()
		text = re.sub(r'<(BR|br)>', '\n', text)	# 替换html中的br换行符
		text = re.sub(r'<.*?>', '', text)		# 替换穿插在法律内容中的html标签对
		text = re.sub(r'&nbsp;', '', text)		# 替换html中的空白字符
		with open('36stratagem/第%s计-%s.txt' % (stratagem[0], stratagem[2]), 'w') as f:
			f.write(text)

if __name__ == "__main__":
	save_36stratagem()
