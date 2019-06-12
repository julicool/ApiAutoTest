from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib


def send_mail(my_time):
    # 设置服务器信息
    my_host = "smtp.126.com"
    my_user = "julicool@126.com"
    my_pass = "ZHAOJIAQI0628"

    # 设置发/收件人
    sender = "julicool@126.com"
    receivers = ['julicool@126.com']

    # 设置邮件内容
    mail_message = MIMEMultipart()
    mail_message['To'] = "julicool@126.com"
    mail_message['Subject'] = Header('AutoTest执行情况', 'utf-8')
    mail_message.attach(MIMEText('最新测试执行时间'+my_time+'\n'+'请及时检查附件结果', 'plain', 'utf-8'))

    # 设置附件
    mail_file = MIMEText(open('./Results/report-' + my_time + '.xls', 'rb').read(), 'base64', 'utf-8')
    mail_file["Content-Type"] = 'application/octet-stream'
    mail_file["Content-Disposition"] = 'attachment; filename="report-' + my_time + '.xls"'
    mail_message.attach(mail_file)

    # 邮件发送
    try :
        mail_smtp = smtplib.SMTP()
        mail_smtp.connect(my_host, 25)
        mail_smtp.ehlo()
        mail_smtp.starttls()
        mail_smtp.login(my_user, my_pass)
        mail_smtp.sendmail(sender, receivers, mail_message.as_string())
        return "邮件发送成功"
    except smtplib.SMTPException as e:
        return e
