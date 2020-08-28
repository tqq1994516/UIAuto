# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password
    # 发送 ===改动位置  所使用邮箱smtp服务
    # email_host = "smtp.163.com"
    email_host = "smtp.qq.com"
    send_user = "2717778598@qq.com"
    password = "siwsemxvtoitdejj"
# Sub 是指  用户主题
    # Content 是指内容
    # user_list是用户列表
    @staticmethod
    def send_mail(user_list, sub, content):
        user = "zhuque"+"<"+send_user+">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
    # 因为收件人列表是;分割
        message['To'] = ";".join(user_list)
        # 使用smtp服务器  pop3接收
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main2(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        # 90%
        # 留个百分号
        pass_result = "%.2f%%" % (pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num/count_num*100)
        user_list = ['602253060@qq.com']
        sub = "UI自动化测试报告"
        content = "运行用例总数%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    user_list1 = ['602253060@qq.com']
    sub1 = "这是个6.27测试邮件"
    content1 = "这是第一封测试邮件"
    # sen.send_mail(user_list,sub,content)
    # sen.send_main2([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])
