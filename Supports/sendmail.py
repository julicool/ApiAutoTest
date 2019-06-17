from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib


def send_mail(run_result):
    # 设置服务器信息
    my_host = "smtp.126.com"
    my_user = "julicool@126.com"
    my_pass = "ZHAOJIAQI0628"

    # 设置收\发件人
    receivers = ['julicool@126.com']
    sender = "julicool@126.com"

    # 设置邮件内容
    mail_message = MIMEMultipart()
    mail_message['To'] = "julicool@126.com"
    mail_message['Subject'] = Header('AutoTest执行情况', 'utf-8')
    mail_comtent = '<h2>今日执行情况</h2><hr width=33% align="left" /><p style="font: 16px">执行失败<span style="color: red;font-weight: 600"> ' + str(run_result['run_failt']) +'</span></p><p style="font: 16px">执行总数<span style="font-weight: 600"> ' + str(run_result['run_total']) + '</span></p>'
    mail_message.attach(MIMEText(mail_comtent, 'html', 'utf-8'))

    # 设置附件
    mail_file = MIMEText(open('./Results/report-' + str(run_result['run_time']) + '.xls', 'rb').read(), 'base64', 'utf-8')
    mail_file["Content-Type"] = 'application/octet-stream'
    mail_file["Content-Disposition"] = 'attachment; filename="report-' + str(run_result['run_time']) + '.xls"'
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
