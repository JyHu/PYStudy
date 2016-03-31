#coding:utf-8



import smtplib


'''

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。


SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]

from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息

'''


sender = 'aug_88@163.com'
receiver = 'aug_88@163.com'

message = '''From: From Person <aug_88@163.com>
To: To Person <aug_88@163.com>
Subject: SMTP e-mail test

This is a test e-mail message.

'''

try:
	smtpObj = smtplib.SMTP('192.168.41.99')
	smtpObj.sendmail(sender, receiver, message)
	print 'successfully sent memail'
except Exception, e:
	print 'error : unable to send email'
else:
	pass
finally:
	pass