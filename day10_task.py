# -*- coding: utf-8 -*-
# @Time : 2021/9/23 17:21
# @Author : 小菜鸡儿
# @FileName: day10_task.py
# @Software: PyCharm
'''super关键字的使用和继承中方法的调用'''
# class Oldphone:
#     __brand=''
#     def setBrand(self,brand):
#         self.__brand=brand
#     def getBrand(self):
#         return self.__brand
#     def call(self,number):
#         print("正在给"+number+"打电话...")
# class Newphone(Oldphone):
#     def call(self,number):
#         print("语音拨号中......")
#         super().call(number)
#     def show(self):
#         print("品牌为："+super().getBrand()+"的手机很好用...")
# if __name__=='__main__':
#     n=Newphone()
#     n.setBrand('华为')
#     n.show()
#     n.call('13552648187')
'''继承的传递性'''
# class Chef:
#     __name=''
#     __age=0
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name
#     def setAge(self,age):
#         if age<=0 or age>100:
#             print("年龄输入有误,请重新输入！")
#         else:
#             self.__age=age
#     def getAge(self):
#         return self.__age
#     def steamRice(self):
#         print(self.__name+"正在蒸饭...")
# class headChef(Chef):
#     def dishes(self):
#         print(super().getName()+"正在炒菜...")
# class friedDish(headChef):
#     def steamRice(self):
#         print(super().getName()+"正在蒸面条...")
#     def dishes(self):
#         print(super().getName()+"正在炒土豆...")
# if __name__=='__main__':
#     f=friedDish()
#     f.setName('嘿嘿')
#     f.setAge(50)
#     print(f.getName(),f.getAge())
#     f.steamRice()
#     f.dishes()
'''
i.人：年龄，性别，姓名
ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类
iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现
'''
class Person:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
class Worker(Person):
    def __init__(self,name,sex,age):
        super().__init__(name,sex,age)
    def show(self):
        pass
    def work(self):
        print("工人"+self.name+"正在砌墙...")
class Student(Person):
    def __init__(self,sno,sname,sex,age):
        self.sno=sno
        super().__init__(sname,sex,age)
    def show(self):
        pass
    def learn(self):
        print("学生"+self.name+"正在敲代码...")
    def sing(self):
        print("学生"+self.name+"正在一边儿敲代码一边儿哼小曲儿...")
if __name__=='__main__':
    w=Worker('嘿呦','男',55)
    w.work()
    s=Student('s001','小菜鸡儿','女',20)
    s.learn()
    s.sing()

