import random
'''
实现输入10个数字，并打印10个数的求和结果
'''
# re=0
# for i in range(10):
#     a=int(input("请输入第{}个数字：".format(i+1)))
#     re=re+a
# print(re)

'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
'''
# l=[]
# for i in range(10):
#     a=int(input("请输入第{}个数字：".format(i+1)))
#     l.append(a)
# print("最大值为：",max(l))
# print("和为：",sum(l))
# print("平均数为：",sum(l)/len(l))

'''
使用random模块，如何产生 50~150之间的数？
'''
# num=random.randint(50,150)
# print(num)

'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形）
'''
# a=int(input("请输入三角形的第一条边："))
# b=int(input("请输入三角形的第二条边："))
# c=int(input("请输入三角形的第三条边："))
# if a+b>c and a-b<c:
#     print("能构成三角形")
#     if a==b==c:  #因为等边三角形是特殊的等腰三角形，所以需要先判断等边
#         print("能构成等边三角形")
#     elif a==b or a==c or b==c:
#         print("能构成等腰三角形")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print("能构成直角三角形")
#     else:
#         print("能构成普通三角形")
# else:
#     print("不能构成三角形")

'''
使用+，-号实现两个数的调换
'''
# a=56
# b=78
# a=a+b
# b=a-b
# a=a-b
# print("a的值为%d,b的值为%d"%(a,b))

# a=a-b
# b=a+b
# a=b-a
# print("a的值为%d,b的值为%d"%(a,b))

'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
# username='root'
# password='admin'
# print("----------------欢迎进入登录页面-------------------")
# u=input("请输入用户名：")
# p=input("请输入密码：")
# if p==password:
#     print("-------------------登陆成功-----------------------")
# elif p!=password:
#     p1=input("密码错误，请重新输入密码：")
#     if p1==password:
#         print("---------------------登陆成功---------------------")
#     elif p1!=password:
#         p2=input("密码错误，请重新输入密码：")
#         if p2==password:
#             print("---------------------登陆成功--------------------")
#         else:
#             print("-------------密码错误，账户已被锁定！---------------")

'''
编程实现三角形图形打印
'''


'''
使用while循环实现99乘法表的打印
'''
# i=1
# while i<=9:
#     j = 1
#     while j<=i:
#         print("{}*{}={}".format(i,j,i*j),end="\t")
#         j+=1
#     print("\n")
#     i+=1

'''
编程实现99乘法表的倒叙打印
'''
# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print("%d*%d=%d"%(j,i,i*j),end="\t")
#         j+=1
#     print("\n")
#     i-=1

'''
一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
'''
# n=0
# high=-20
# up=3
# down=-2
# while high<=0:
#     n=n+1
#     high = high + up
#     print(high)
#     if high>0:
#         print("第%d天能出来" % (n))
#     else:
#         high = high + down
#         print(high)
#         if high>0:
#             print("第%d天能出来" % (n))

'''
继续完成上午的猜数字游戏的需求功能
1.添加计数打印功能
2.添加次数金币功能和锁定系统功能
'''
# n=0
# num=random.randint(0,10)
# print("-----------------欢迎进入猜数游戏-----------------")
# while 1:
#     n+=1
#     a=int(input("请输入猜测的数字："))
#     if a>num:
#         print("猜大了，稍微小点儿！")
#     elif a<num:
#         print("猜小了，大方点儿！")
#     else:
#         print("恭喜你，猜对了！")
#         print("一共猜了%d次"%(n))
#         print("---------------------游戏结束--------------------")
#         break

# n=0
# money=100
# num=random.randint(0,9)
# print("--------------------欢迎进入猜数游戏----------------------")
# while money>0:
#     n+=1
#     money=money-10
#     a=int(input("请输入一个数字："))
#     if a==num:
#         print("恭喜你，中奖了！")
#         print("一共猜了%d次"%(n))
#         print("游戏结束~~~~~~~~~")
#         break
#     elif money==0:
#         print("余额不足，请充值后再来玩儿！！！")
#         print("-----------------------系统已锁定------------------------")
#         input("按Enter键退出系统。。。。。。")
#         break
#     else:
#         print("很遗憾，没中奖！")
#         print("------------------------游戏继续-------------------------")

'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
0的阶乘为1；负数没有阶乘
'''
j=1
mul=1
re=0
for i in range(1,21):
    # print(i)
    if j<=i:
        mul*=j
        j+=1
    re+=mul
print(re)
