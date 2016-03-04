#coding=utf-8

__author__ = 'JinyouHU'

import smtplib
from email.mime.text import MIMEText


mailto_list = ["aug_88@163.com"]
mail_host = 'smtp.163.com'
mail_user = 'aug_88'
mail_pass = '密码'
mail_postfix = '163.com'


def send_mail(to_list, sub, content):
    me = 'hello' + '<' + mail_user + '@' + mail_postfix + '>'
    msg = MIMEText(content, _subtype='html', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == '__main__':
    mail_body = "<a href='http://www.cnblogs.com'>哈哈哈</a>"
    if send_mail(mailto_list, 'hello00000', mail_body):
        print '发送成功'
    else :
        print '发送失败'