# -*- coding: UTF-8 -*-
 
# 如何添加附件
import os
 
 
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


os.chdir("C:\\Users\\h****m\\Desktop\\Auto_email")
 
 
def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
 '''
 @subject:邮件主题
 @msg:邮件内容
 @toaddrs:收信人的邮箱地址
 @fromaddr:发信人的邮箱地址
 @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
 @password:发信人的邮箱密码
 '''
 
 
 mail_msg = MIMEMultipart()
 if not isinstance(subject,unicode): #过滤或者不过滤貌似没啥影响
  subject = unicode(subject, 'utf-8')
 mail_msg['Subject'] = subject
 mail_msg['From'] =fromaddr
 mail_msg['To'] = ','.join(toaddrs)
 #mail_msg.attach(MIMEText(msg, 'plain', 'utf-8')) #f发送文本文件
 mail_msg.attach(MIMEText(msg, 'html', 'utf-8')) #发送html格式邮件
  
 #构造附件1
 att1=MIMEText(open("test_file1.txt",'rb').read(),'base64','utf-8') #注意：直接读取中文文件名会报错 
 att1["Content-Type"] = 'application/octet-stream'
 att1["Content-Disposition"] = 'attachment; filename="test_file1.txt"'
 mail_msg.attach(att1)
  
  
 #构造附件2：添加中文附件名
 att2=MIMEText(open(u'测试文件2.docx','rb').read(),'base64','utf-8')
 att2["Content-Type"] = 'application/octet-stream'
 att2["Content-Disposition"] = 'attachment; filename="test_file2.docx"'
 mail_msg.attach(att2)
  
 try:
  s = smtplib.SMTP()
  s.connect(smtpaddr) #连接smtp服务器
  s.login(fromaddr,password) #登录邮箱
  s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件
  s.quit()
  print "邮件发送成功！"
 except Exception,e:
  print "Error: unable to send email"
  print traceback.format_exc()
 
 
if __name__ == '__main__':
 fromaddr = "h****m@126.com"
 smtpaddr = "smtp.126.com"
 toaddrs = ["83****789@qq.com","h****m@126.com"]
 subject = "Hello,我是邮件主题"
 password = "不能告诉你"
 #msg = "Hello,我是邮件内容 !!!"
 msg="""
 <p>Python 邮件发送测试...</p>
 <p><a href=http://www.runoob.com >这是一个链接</a></p>
 """
 sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)