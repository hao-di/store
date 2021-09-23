# -*- coding: utf-8 -*-
# @Time : 2021/9/22 16:00
# @Author : 小菜鸡儿
# @FileName: day09_task.py
# @Software: PyCharm
'''定义一个空调类'''
# class Air:
#     __brand=""
#     __price=0.0
#     __time=0
#     def setBrand(self,brand):
#         self.__brand=brand
#     def getBrand(self):
#         return self.__brand
#     def setPrice(self,price):
#         if price<=0:
#             print("输入价格非法,请重新输入！")
#         else:
#             self.__price=int(price)
#     def getPrice(self):
#         return self.__price
#     def setTime(self,time):
#         if time<0:
#             print("时间输入有误,请重新输入！")
#         else:
#             self.__time=int(time)
#     def getTime(self):
#         return self.__time
#     def open(self):
#         print(self.__brand,"空调开机了......")
#     def stop(self,time):
#         print("空调将在",self.__time,"分钟后自动关闭...")
#     def show(self):
#         print("空调的品牌是",self.__brand,"空调价格为",self.__price,"元")
# a=Air()
# a.setBrand("海尔")
# a.setPrice(1000)
# a.open()
# a.show()
# a.stop(2)
'''定义一个学生类'''
# class Student:
#     __name=''
#     __age=0
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name
#     def setAge(self,age):
#         if age<=0 or age>100:
#             print("年龄输入非法,请重新输入！")
#         else:
#             self.__age=age
#     def getAge(self):
#         return self.__age
#     def show(self):
#         print("大家好,我叫",self.__name,",今年",self.__age,"岁了！")
#     def compare(self,Student):
#         if Student.__age>self.__age:
#             return "我比同桌小"+str(Student.__age-self.__age)+"岁！"
#         elif Student.__age<self.__age:
#             return "我比同桌大"+str(self.__age-Student.__age)+"岁！"
#         else:
#             return "我和同桌一样大！"
# me=Student()
# me.setName('小菜鸡儿')
# me.setAge(20)
# tab=Student()
# tab.setName('小乳猪')
# tab.setAge(19)
# me.show()
# print(me.compare(tab))
'''打电话业务逻辑'''
# class People:
#     __name=''
#     __gender=''
#     __age=0
#     __charge=0.0
#     __brand=''
#     __battery=0
#     __size=0
#     __standby=0
#     __integral=0
#     __number=''
#     __last=0
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name
#     def setGender(self,gender):
#         if gender=='男' or gender=='女':
#             self.__gender=gender
#         else:
#             print("性别输入非法,请重新输入！")
#     def getGender(self):
#         return self.__gender
#     def setAge(self,age):
#         if age<=0 or age>100:
#             print("年龄输入非法,请重新输入！")
#         else:
#             self.__age=age
#     def getAge(self):
#         return self.__age
#     def setCharge(self,charge):
#         self.__charge=float(charge)
#     def getCharge(self):
#         return self.__charge
#     def setBrand(self,brand):
#         self.__brand=brand
#     def getBrand(self):
#         return self.__brand
#     def setBattery(self,battery):
#         self.__battery=battery
#     def getBattery(self):
#         return self.__battery
#     def setSize(self,size):
#         if size<=0:
#             print("屏幕大小输入非法,请重新输入！")
#         else:
#             self.__size=size
#     def getSize(self):
#         return self.__size
#     def setSendby(self,sendby):
#         if sendby<0:
#             print("最大待机时长输入非法,请重新输入！")
#         else:
#             self.__sendby=sendby
#     def getSendby(self):
#         return self.__sendby
#     def setIntegral(self,integral):
#         if integral<0:
#             print("积分不能为负数,请重新输入！")
#         else:
#             self.__integral=integral
#     def getIntegral(self):
#         return self.__integral
#     def setNumber(self,number):
#         self.__number=number
#     def getNumber(self):
#         return self.__number
#     def setLast(self,last):
#         if last<0:
#             print("通话时长不能小于0,请重新输入！")
#         else:
#             self.__last=last
#     def getLast(self):
#         return self.__last
#     def show(self):
#         pass
#     def send(self,content):
#         print("您所发送的短信内容为：",content)
#     def call(self,number,last):
#         # print(number,last)
#         if len(number)==0:
#             return "号码不能为空,请重新输入！"
#         else:
#             if self.__charge<1:
#                 return "余额不足,请充值后再拨打！"
#             else:
#                 if last>=0 or last<10:
#                     self.__charge-=last*1
#                     self.__integral+=last*15
#                     return "本次通话扣费￥"+str(last*1)+",增加积分"+str(last*15)
#                 elif last>=10 or last<20:
#                     self.__charge-=last*0.8
#                     self.__integral+=last*39
#                     return "本次通话扣费￥"+str(last*0.8)+",增加积分"+str(last*39)
#                 else:
#                     self.__charge-=last*0.65
#                     self.__integral+=last*48
#                     return "本次通话扣费￥"+str(last*0.65)+",增加积分"+str(last*48)
# if __name__=='__main__':
#     p=People()
#     p.setCharge(10)
#     p.setNumber(input("请输入要呼叫的电话号码："))
#     # number=p.getNumber()
#     p.setLast(int(input("请输入您要通话的时长：")))
#     # last=p.getLast()
#     print(p.call(p.getNumber(),p.getLast()))

'''分析一个水杯的属性和功能,使用类描述并创建对象(高度，容积，颜色，材质; 能存放液体)'''
# class Cup:
#     # __high=0.0
#     # __volume=0.0
#     # __color=''
#     # __texture=''
#     def __init__(self,high,volume,color,texture):
#         self.__high=high
#         self.__volume=volume
#         self.__color=color
#         self.__texture=texture
#     # def setHigh(self,high):
#     #     if high<=0:
#     #         print("高度输入非法,请重新输入！")
#     #     else:
#     #         self.__high=high
#     # def getHigh(self):
#     #     return self.__high
#     # def setVolume(self,volume):
#     #     if volume<=0:
#     #         print("容积输入非法,请重新输入！")
#     #     else:
#     #         self.__volume=volume
#     # def getVolume(self):
#     #     return self.__volume
#     # def setColor(self,color):
#     #     self.__color=color
#     # def getColor(self):
#     #     return self.__color
#     # def setTexture(self,texture):
#     #     self.__texture=texture
#     # def getTexture(self):
#     #     return self.__texture
#     def storeliquid(self):
#         if self.__high>0 and self.__volume>0:
#             print("俺是一只身高"+str(self.__high)+"cm容积为"+str(self.__volume)+"ml,穿着"+self.__color
#                   +"衣服"+"用"+self.__texture+"做成的小水杯,你可以用俺喝水哦~")
#         else:
#             print("输入有误,请重新输入！")
# if __name__=='__main__':
#     c=Cup(-20,300,'绿色','玻璃')
#     # c=Cup()
#     # c.setHigh(20)
#     # c.setVolume(300)
#     # c.setColor('绿色')
#     # c.setTexture('玻璃')
#     c.storeliquid()
'''有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）'''
# class Computer:
#     # __name=''
#     # __size=0
#     # __price=0.0
#     # __cputype=''
#     # __memsize=0.0
#     # __standby=0
#     def __init__(self,name,size,price,cputype,memsize,standby):
#         self.__name=name
#         self.__size=size
#         self.__price=price
#         self.__cputype=cputype
#         self.__memsize=memsize
#         self.__standby=standby
#     # def setName(self,name):
#     #     self.__name=name
#     # def getName(self):
#     #     return self.__name
#     # def setSize(self,size):
#     #     if size<=0:
#     #         print("屏幕大小输入非法,请重新输入！")
#     #     else:
#     #         self.__size=size
#     # def getSize(self):
#     #     return self.__size
#     # def setPrice(self,price):
#     #     if price<=0:
#     #         print("价格输入有误,请重新输入！")
#     #     else:
#     #         self.__price=price
#     # def getPrice(self):
#     #     return self.__price
#     # def setCputype(self,cputype):
#     #     self.__cputype=cputype
#     # def getCputype(self):
#     #     return self.__cputype
#     # def setMemsize(self,memsize):
#     #     if memsize<=0:
#     #         print("内存大小输入有误,请重新输入！")
#     #     else:
#     #         self.__memsize=memsize
#     # def getMemsize(self):
#     #     return self.__memsize
#     # def setStandby(self,standby):
#     #     if standby<=0:
#     #         print("待机时长输入有误,请重新输入！")
#     #     else:
#     #         self.__standby=standby
#     # def getStandby(self):
#     #     return self.__standby
#     def show(self):
#         if self.__size>0 and self.__price>0 and self.__standby>0 and self.__memsize>0:
#             print("--------------以下是该笔记本的详细信息-----------")
#             info='''
#                     笔记本名字：%s
#                     屏幕大小：%s
#                     价格：%s
#                     cup型号：%s
#                     内存大小：%s
#                     待机时长：%s
#                  '''
#             print(info%(self.__name,self.__size,self.__price,self.__cputype,self.__memsize,self.__standby))
#         else:
#             print("输入有误,请重新输入！")
#     def typewriting(self):
#         print("我正在用"+self.__name+"笔记本打字......")
#     def playgames(self):
#         print("我正在用"+self.__name+"笔记本打游戏......")
#     def watchvideo(self):
#         print("我正在用"+self.__name+"笔记本看视频......")
# if __name__=='__main__':
#     c=Computer('惠普',14,5000,'Intel酷睿i7 4510U',8,3)
#     # c=Computer()
#     # c.setName('惠普')
#     # c.setSize(14)
#     # c.setPrice(5000)
#     # c.setCputype('Intel酷睿i7 4510U')
#     # c.setMemsize(8)
#     # c.setStandby(3)
#     c.show()
#     c.typewriting()
#     c.playgames()
#     c.watchvideo()
'''
定义了一个学生类：
属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码
行为:学习(要求参数传入学习的时间),玩游戏(要求参数传入游戏名),编程(要求参数传入写代码的行数),数的求和(要求参数用变长参数来做,返回求和结果)
'''
# class Student:
#     def __init__(self,sno,sname,age,sex,high,weight,score,add,tel):
#         self.__sno=sno
#         self.__sname=sname
#         self.__age=age
#         self.__sex=sex
#         self.__high=high
#         self.__weight=weight
#         self.__score=score
#         self.__add=add
#         self.__tel=tel
#     def show(self):
#         if (self.__age>0 and self.__age<100) and (self.__sex=='男' or self.__sex=='女') and\
#             (self.__high>0 and self.__high<2) and self.__weight>0 and self.__score>=0:
#             print("---------------------以下是该生的详细信息----------------")
#             info='''
#                   学号：%s
#                   姓名：%s
#                   年龄：%s
#                   性别：%s
#                   身高：%s m
#                   体重：%s kg
#                   成绩：%s
#                   家庭地址：%s
#                   电话号码：%s
#                  '''
#             print(info%(self.__sno,self.__sname,self.__age,self.__sex,self.__high,self.__weight,self.__score,self.__add,self.__tel))
#         else:
#             print("输入有误,请重新输入！")
#     def learn(self,time):
#         if time>=0:
#             print(self.__sname+"已经学习了"+str(time)+"小时......")
#         else:
#             print("学习时长输入有误,请重新输入!")
#     def playgames(self,game):
#         print(self.__sname+"正在玩儿"+game)
#     def code(self,num):
#         if num>=0:
#             print(self.__sname+"写了"+str(num)+"行代码")
#         else:
#             print("代码行数输入有误,请重新输入！")
#     def add(self,*tu):
#         sum=0
#         for i in tu:
#             sum+=i
#         return sum
# if __name__=='__main__':
#     s=Student('s001','小菜鸡儿',20,'女',1.6,50,20,'北京市昌平区',123456)
#     s.show()
#     s.learn(3)
#     s.playgames('开心消消乐')
#     s.code(0)
#     # print(s.add(1, 2, 3))
'''
车类：
属性：车型号，车轮数，车身颜色，车重量，油箱存储大小
功能：跑（要求参数传入车的具体功能，比如越野，赛车）
创建：法拉利，宝马，铃木，五菱，拖拉机对象
'''
# class Car:
#     def __init__(self,brand,num,color,weight,cap):
#         self.__brand=brand
#         self.__num=num
#         self.__color=color
#         self.__weight=weight
#         self.__cap=cap
#     def show(self):
#         if self.__num>0 and self.__weight>0 and self.__cap>=0:
#             print("车型：",self.__brand,",车轮数：",self.__num,",车身颜色：",self.__color,",车重：",self.__weight,"kg,油箱容量：",self.__cap,"l")
#         else:
#             print("信息输入有误,请重新输入！")
#     def run(self,func):
#         print(self.__brand+"能"+func)
# if __name__=='__main__':
#     F=Car('法拉利',4,'pink',1472,78)
#     F.show()
#     F.run('赛车')
#     B=Car('宝马',4,'pink',1472,78)
#     B.show()
#     B.run('通勤')
#     L=Car('铃木',4,'pink',1472,78)
#     L.show()
#     L.run('越野')
#     W=Car('五菱',4,'pink',1472,78)
#     W.show()
#     W.run('越野')
#     T=Car('拖拉机',4,'pink',1472,78)
#     T.show()
#     T.run('拉货')
'''
笔记本：
属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小
行为：打游戏（传入游戏的名称）,办公
'''
# class Computer:
#     def __init__(self,brand,standby,color,weight,cputype,memsize,hdsize):
#         self.__brand=brand
#         self.__standby=standby
#         self.__color=color
#         self.__weight=weight
#         self.__cputype=cputype
#         self.__memsize=memsize
#         self.__hdsize=hdsize
#     def show(self):
#         if self.__standby>0 and self.__weight>0 and self.__memsize>0 and self.__hdsize>0:
#             info='''
#                   笔记本型号：%s
#                   待机时间：%sh
#                   颜色：%s
#                   重量：%skg
#                   cpu型号：%s
#                   内存大小；%sGB
#                   硬盘大小：%sGB
#                  '''
#             print(info%(self.__brand,self.__standby,self.__color,self.__weight,self.__cputype,self.__memsize,self.__hdsize))
#     def playgames(self,game):
#         print("小菜鸡儿正在用"+self.__brand+"笔记本玩儿"+game)
#     def work(self):
#         print("小菜鸡儿正在用"+self.__brand+"笔记本办公......")
# if __name__=='__main__':
#     c=Computer('联想T430',2,'black',2.18,'Core酷睿i5',8,500)
#     c.show()
#     c.playgames('植物大战僵尸')
#     c.work()
'''
猴子类：
属性:类别，性别，身体颜色，体重
行为:造火(要求传入造火的材料:比如木棍还是石头),学习事物(要求参数传入学习的具体事物,可以不止学习一种事物)
'''
class Monkey:
    def __init__(self,category,gender,color,weight):
        self.__category=category
        self.__gender=gender
        self.__color=color
        self.__weight=weight
    def show(self):
        if (self.__gender=='male' or self.__gender=='female') and self.__weight>0:
            print("俺是一只小猴子,俺属于"+self.__category+",俺嘞性别是"+self.__gender+",俺的毛是"+self.__color,
                  "色,俺体重是"+str(self.__weight)+"kg")
        else:
            print("输入有误,请重新输入！")
    def makefire(self,materials):
        print(self.__category+"会用"+materials+"造火......")
    def learn(self,*thing):
        for i in thing:
            print(self.__category+"正在学习"+i+"......")
if __name__=='__main__':
    m=Monkey('懒猴','male','black',1.5)
    m.show()
    m.makefire('木棍')
    m.learn('唱歌','说话')