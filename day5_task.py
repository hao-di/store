info='''
        *********************************************
        *            中国工商银行账户管理系统V1.0        *
        *********************************************
        *                   1、开户                  *
        *                   2、存钱                  *
        *                   3、取钱                  *
        *                   4、转账                  *
        *                   5、查询                  *
        *                   6、退出                  *
        *********************************************
'''
print(info)
import random
bank={}
#{'Frank': {'account': 15394946, 'password': '123456', 'country': '中国', 'province': '北京', 'street': '起码路', 'door': '001', 'money': 0, 'bank_name': '工商银行起码路分行'}}
bank_name="工商银行起码路分行"
#                 一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100 :return 3#bank_adduer=3
    if username in bank:return 2#bank_adduer=2
    bank[username]={
        "account": account,#键：你输入的值account=random.randint(10000000,99999999)
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    print(bank)
    return 1#bank_adduer=1
def adduser():
    username=input("请输入您的用户名：")
    password = input("请输入您的密码：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜你开户成功下面是你的信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：********
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    else:
        print("开户失败，用户已存在，请重新输入！")

def IN_account():
    username=input("请输入您的用户名：")
    IN_money=int(input("请输入您的存入金额："))
    status=deposit(username,IN_money)
    if status==True:
        print("存款成功！"+"您的账户余额为：",bank[username]['money'])
    else:
        print("输入有误，请重新输入！")
def deposit(username,IN_money):
    if username not in bank or IN_money<0: return False
    # if username in bank and IN_money>=0:
    bank[username]['money']+=IN_money
    return True

def OUT_account():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    OUT_money=int(input("请输入您的取款金额："))
    status=withdraw(username,password,OUT_money)
    if status==1:
        print("账户不存在，请重新输入！")
    elif status==2:
        print("密码错误，请重新输入！")
    elif status==3:
        print("取款金额输入有误，请重新输入取款金额！")
    else:
        print("取款成功！"+"您的账户余额为：",bank[username]['money'])
def withdraw(username,password,OUT_money):
    if username not in bank:
        return 1
    else:
        if password!=bank[username]['password']:
            return 2
        else:
            if OUT_money>bank[username]['money'] or OUT_money<=0:
                return 3
            else:
                bank[username]['money']-=OUT_money
                return 0

def IO_transfer():
    OUT_username=input("请输入转出账户：")
    OUT_password=input("请输入转出账户的密码：")
    IN_username=input("请输入转入账户：")
    OUT_money=int(input("请输入转出的金额："))
    status=tranfer(OUT_username,IN_username,OUT_password,OUT_money)
    if status == 1:
        print("账户输入有误，请重新输入！")
    elif status==2:
        print("密码错误，请重新输入！")
    elif status==3:
        print("转账金额输入有误，请重新输入转账额度！")
    else:
        print("转账成功！"+"您的账户余额为：",bank[OUT_username]['money'])
def tranfer(OUT_username,IN_username,OUT_password,OUT_money):
    if OUT_username not in bank or IN_username not in bank or OUT_username==IN_username:
        return 1
    else:
        if OUT_password!=bank[OUT_username]['password']:
            return 2
        else:
            if OUT_money>bank[OUT_username]['money'] or OUT_money<=0:
                return 3
            else:
                bank[OUT_username]['money']-=OUT_money
                bank[IN_username]['money']+=OUT_money
                return 0

def re_inquiry():
    username=input("请输入要查询的账户名：")
    password=input("请输入账户密码：")
    inquiry(username, password)

def inquiry(username,password):
    if username not in bank:
        print("该用户不存在，请重新输入！")
    else:
        if password != bank[username]['password']:
            print("密码错误，请重新输入！")
        else:
            print("查询成功，下面是您的账户信息：")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：********
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            print(info % (username, bank[username]['account'], bank[username]['country'],bank[username]['province'] ,bank[username]['street'],bank[username]['door'],bank[username]["money"], bank_name))

while True:
    begin=input("请输入业务号：")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、存钱")
        IN_account()
    elif  begin == "3":
        print("3、取钱")
        OUT_account()
    elif  begin == "4":
        print("4、转账")
        IO_transfer()
    elif  begin == "5":
        print("5、查询 ")
        re_inquiry()
    elif  begin == "6":
        print("6、退出")
        break

