#coding:utf-8



import urllib



'''


urlretrieve(url, name)	
参数一：要获取资源的地址
参数二：保存在本地时的文件名字，可以为空，但是不建议


返回一个元组：(filename, headers)
1：文件名
2：远程文件的信息


'''



rec = urllib.urlretrieve('http://www.yw11.com/namelist.php', 'page.html')	
print rec[1]
print rec[0]


