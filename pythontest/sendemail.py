#! /usr/bin/env python
import smtplib
from email.mime.text import MIMEText

mailto_list=['annie_zhang510@163.com']
mail_host="smtp.163.com"
mail_user="annie_zhang510@163.com"
mail_pass="ZKX@510tiancai"
mail_postfix="postfix"
def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
for i in range(5):
    if send_mail(mailto_list,"hello","haha!"):
        print "done!"
    else:
        print "failed!"