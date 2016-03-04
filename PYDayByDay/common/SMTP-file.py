#coding=utf-8

__author__ = 'JinyouHU'


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('/Users/k/Desktop/mkprogress.txt', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="mk.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('/Users/k/Desktop/f2.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="f2.txt"'
msg.attach(att2)

#加邮件头
msg['to'] = 'aug_88@163.com'
msg['from'] = 'aug_88@163.com'
msg['subject'] = 'hello world'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.163.com')
    server.login('aug_88','')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print "发送成功"
except Exception, e:
    print str(e)