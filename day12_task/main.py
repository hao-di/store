'''
    HTMLTestRunner：运行器，可以运行和生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import  unittest
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib

# 任务1：代码邮箱发送
# 任务2：减法，除法，乘法用例写出来。
# 4.代码 163 发送邮件，将报告添加为附件，发送给我13552648187@163.com
# 密码不是登陆密码，邮箱对第三方软件的授权码

# ==============定义发送邮件==========
def send_mail(file_new):
    #-----------1.跟发件相关的参数------
    smtpserver = 'smtp.qq.com'                #发件服务器
    port = 25                      #端口
    username = '3209028245@qq.com'  #发件箱用户名
    password = 'kqoprnihafhaddce'        #发件箱密码
    sender = '3209028245@qq.com'    #发件人邮箱
    receiver = '1728491289@qq.com' #收件人邮箱
    # receiver = '2431320433@qq.com'
    # ----------2.编辑邮件的内容------
    #读文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("计算器测试报告", 'utf-8').encode()#主题
    msg['From'] = Header(sender)                #发件人
    msg['To'] = Header(receiver)            #收件人
    # msg['To'] = ';'.join(receiver)   #多人接收时写法
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
    # #发送邮件
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.mxhichina.com')  # 邮箱服务器
    # smtp.login(username, password)  # 登录邮箱
    # smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    # smtp.quit()
    print("邮件已发出！注意查收。")
# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new
if __name__ == "__main__":
    # 1.加载用例
    tests = unittest.defaultTestLoader.discover(r"C:\\Users\\lenovo\\PycharmProjects\\proj1\\tasks\\day12_task",pattern="Test*.py")


    # 2.创建运行器
    runner = HTMLTestRunner.HTMLTestRunner(
        title = "这是计算器测试报告",
        description= "计算器测试报告",
        verbosity=1,
        stream=open(file="计算器报告.html",mode="w+",encoding="utf-8")
    )

    # 3.让运行器运行用例
    runner.run(tests)
    # 获取当前时间
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    #测试报告文件夹
    test_path = 'C:\\Users\\lenovo\\PycharmProjects\\proj1\\tasks\\day12_task'
    new_report = new_report(test_path)
    send_mail(new_report)  # 发送测试报告


# coding:utf-8

# def send_email():
#     smtpserver = "smtp.qq.com"  # 发送服务器
#     port = 25  # 端口
#     sender = "3209028245@qq.com"  # 寄件人账号
#     psw = "kqoprnihafhaddce"  # 授权码密码（在邮箱设置里面设置）
#     receiver = ['1728491289@qq.com', '3209028245@qq.com']  # 接受者
#     subject = "主题：这是一个计算器测试报告"
#
#     # 创建一个带附件的实例
#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] = ';'.join(receiver)  # 多人接收时写法
#     msg['Subject'] = subject
#
#     # 构造附件：
#     # 先读附件
#     test_report = os.path.join(os.path.dirname(os.path.realpath(__file__)), "计算器报告.html")
#     with open(test_report, "rb") as fp:
#         mail_body = fp.read()
#     # 邮件正文内容：
#     # msg.attach(MIMEText("这是一个带附件的邮件", 'plain', 'utf-8')) #正文是以文字存在时
#     msg.attach(MIMEText(mail_body, 'html', 'utf-8'))  # 正文以html存在时
#     # 以下是写附件的格式：
#     att = MIMEText(mail_body, "base64", 'utf-8')
#     att["Content-Type"] = 'application/octet-stream'
#     att["Content-Disposition"] = 'attachment;filename="report_test.html"'  # filename是重名附件名字
#     msg.attach(att)
#
#     # 同时兼容163和QQ邮箱的登录方法
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)
#         smtp.login(sender, psw)  # 登录
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(sender, psw)
#     # smtp.login(sender,psw)              #登录
#     smtp.sendmail(sender, receiver, msg.as_string())  # 发送 as_string 作为字符串类型发送msg['to'].split(",")
#     smtp.quit()
#     print("邮件发送成功！")
#
#
# if __name__ == "__main__":
#     # 1.加载用例
#     tests = unittest.defaultTestLoader.discover(r"C:\\Users\\lenovo\\PycharmProjects\\proj1\\tasks\\day12_task",
#                                                 pattern="Test*.py")
#     # 2.创建运行器
#     runner = HTMLTestRunner.HTMLTestRunner(
#         title="这是计算器测试报告",
#         description="计算器测试报告",
#         verbosity=1,
#         stream=open(file="计算器报告.html", mode="w+", encoding="utf-8")
#     )
#     # 3.让运行器运行用例
#     runner.run(tests)
#     send_email()
