# -*-coding:utf-8-*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 邮件发送的标准模式，具体使用可以百度
def send_mail(run_result):
    # 设置服务器信息
    my_host = "smtp.office365.com"
    my_user = "watchtower@dingtone.me"
    my_pass = "IG4785tower"

    # 设置收\发件人
    receivers = ['topgrowth@dingtone.me']
    sender = "watchtower@dingtone.me"

    # 设置邮件内容
    mail_message = MIMEMultipart()
    mail_message['Subject'] = Header('Ins线上访问监控', 'utf-8')
    mail_comtent = '<p style="font: 16px">执行总数<span style="font-weight: 600"> ' + str(run_result['run_total']) + '</span>，执行失败<span style="color: red;font-weight: 600"> ' + str(run_result['run_fault']) +'</span></p><hr width=33% align="left" />' + get_refult(run_result['run_fault_list'])
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
        return "有执行失败用例，结果报告已通过邮件发送成功"
    except smtplib.SMTPException as e:
        return e

def get_refult(run_fault_list):
    fault_content = "<ul>"
    for i in run_fault_list:
        fault_content = fault_content + "<li>" + i + "</li>"
    fault_content = fault_content + "</ul>"
    return fault_content
