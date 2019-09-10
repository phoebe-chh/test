# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import logging
from logs.logger import Logger
logger = Logger(logger='sendreportbyemail').getlog()
logger.setLevel(level = logging.INFO)
class  SendReportByEmail():
    def __init__(self):
        pass
    def find_report_name(self):
        """查找最后生成的报告文件的路径"""
        #按时间排序
        # os.chdir("/test_reports")
        result_dir = os.path.abspath('..')+"\\test_reports"
        # os.chdir(result_dir)
        lists = os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getctime(result_dir + "\\" + fn))
        file_name = os.path.join(result_dir, lists[-1])
        logger.info(file_name)
        return file_name


    def send_email(self,report_file):
        """发送邮件方法"""
        try:
            # 配置邮件信息
            # 接收邮箱
            receiver = "chenhui-1@thunisoft.com"
            # 发送邮件服务器
            smtp_server = "smtp.thunisoft.com"
            port = "465"
            # 发送邮箱账号和密码（授权码）server_hostname
            username ="chenhui-1@thunisoft.com"
            password ="6789@jkl"
            # os.chdir(r"D:\PycharmProjects\autotest\test_reports")

            # 读取测试报告文件
            mail_body = open(report_file, "r", encoding="utf-8").read()

            # 定义邮件内容
            msg = MIMEMultipart()
            body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
            msg['Subject'] = u"苏州项目自动化测试报告"
            msg['from'] = username
            msg['to'] = receiver
            msg["date"] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
            msg.attach(body)
            # 定义附件内容
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename= "report.html"'
            msg.attach(att)

            # 连接邮箱服务器
            smtp = smtplib.SMTP_SSL(host=smtp_server)
            smtp.connect(host=smtp_server,port=465)
            # 登录邮箱
            smtp.login(username, password)
            # 发送邮件
            smtp.sendmail(username, receiver, msg.as_string())
            # 断开连接
            smtp.quit()
            logger.info("%s 发送成功,查收%s邮箱" % (username, receiver))
        except Exception as e:
            logger.info(e)


    def send_report(self):
        """发送测试报告"""
        # self.send_email(self.find_report_name())
        filename=self.find_report_name()
        logger.info(filename)
        self.send_email(filename)


if __name__ == '__main__':
    t = SendReportByEmail()
    t.send_report()