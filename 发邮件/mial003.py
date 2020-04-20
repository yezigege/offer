"""
参考 廖雪峰：https://www.liaoxuefeng.com/wiki/1016959663602400/1017790702398272
     简书：https://www.jianshu.com/p/cf7241166e33

发送 HTML 邮件
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
# from_addr = input('From: 2274297976@qq.com')
# password = input('Password: dzyxwyk9390')
# 输入收件人地址:
# to_addr = input('To: yezhongqiang@thunder.com.cn')
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ggolswnypgpxdjec')


# 输入Email地址和口令:
from_addr = '2274297976@qq.com'
password = 'ggolswnypgpxdjec'
# 输入收件人地址:
to_addr = 'yezhongqiang@thunder.com.cn'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

"""
构造MIMEText对象时，
第一个参数就是邮件正文，
第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
最后一定要用utf-8编码保证多语言兼容性
"""
# 邮件内容
# msg = MIMEText('hello, send by yezi...', 'plain', 'utf-8')

msg = MIMEText(
    '<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')


# 寄件者
msg['From'] = _format_addr('八十万萝莉总教头: {}'.format(from_addr))
# 收件者
msg['To'] = _format_addr('顾城的叶子: {}'.format(to_addr))
# 邮件主题
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()