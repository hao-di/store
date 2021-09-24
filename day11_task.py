# -*- coding: utf-8 -*-
# @Time : 2021/9/24 15:42
# @Author : 小菜鸡儿
# @FileName: day11_task.py
# @Software: PyCharm
from threading import Thread
import time
box=0
money=3000
price=2
class Cook(Thread):
    name=''
    count=0
    def run(self) -> None:
        global box,money,price
        while True:
            if box>=0 and box<500:
                self.count+=1
                box+=1
                print(self.name,"做好了第",self.count,"个蛋挞,篮子里还剩",box,"个蛋挞！")
            else:
                print("歇会儿,篮子满了......")
                time.sleep(3)
                if box==500:
                    break


class Custom(Thread):
    name=''
    count=0
    def run(self) -> None:
        global box,money,price
        while True:
            if box>0 and money>=price:
                self.count+=1
                box-=1
                money-=price
                print(self.name,"买了",self.count,"个蛋挞,手里还剩",money,"元,篮子里还剩",box,"个蛋挞")
            elif money<price:
                print(self.name,"没钱了,不能买了诶！")
                break
            else:
                print("蛋挞不够了,等会儿再买...")
                time.sleep(2)

c1=Cook()
c2=Cook()
c3=Cook()
c1.name='小菜鸡儿'
c2.name='嘿嘿'
c3.name='嘟嘟'
u1=Custom()
u2=Custom()
u3=Custom()
u4=Custom()
u5=Custom()
u6=Custom()
u1.name='小精豆'
u2.name='老孬蛋'
u3.name='嗯哼'
u4.name='小蚊子'
u5.name='小青椒'
u6.name='小乳猪'
c1.start()
c2.start()
c3.start()
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()















