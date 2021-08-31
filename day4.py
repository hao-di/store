# dict={
#       "北京":{"七马路":{"育荣教育园区":"狼腾测试员"}},
#       "上海":{"浦东新区":{"川沙新镇":"迪士尼"}},
#       "郑州":{"二七路":{"二七广场":"二七塔"}},
#       "南阳":{"邓州":{"人民东路":"花洲书院"}},
#       "洛阳":{"栾川":{"城东":"老君山"}},
#       "杭州":{"西湖区":{"石龙山街":"西湖大学"}}
#       }
# while 1:
#     num=input("请输入一个城市")
#     if  num == "北京":
#         a=input("请输入一个市区")
#         if a  == "七马路":
#             b= input("请输入一个街道")
#             if b == "育荣教育园区":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     elif  num == "上海":
#         a=input("请输入一个市区")
#         if a  == "浦东新区":
#             b= input("请输入一个街道")
#             if b == "川沙新镇":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     elif  num == "郑州":
#         a=input("请输入一个市区")
#         if a  == "二七路":
#             b= input("请输入一个街道")
#             if b == "二七广场":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     elif  num == "南阳":
#         a=input("请输入一个市区")
#         if a  == "邓州":
#             b= input("请输入一个街道")
#             if b == "人民东路":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     elif  num == "洛阳":
#         a=input("请输入一个市区")
#         if a  == "栾川":
#             b= input("请输入一个街道")
#             if b == "城东":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     elif  num == "杭州":
#         a=input("请输入一个市区")
#         if a  == "西湖区":
#             b= input("请输入一个街道")
#             if b == "石龙山街":
#                 print(dict[num][a][b])
#             else:
#                 print("输入有误，请重新输入。。。")
#         else:
#             print("输入有误，请重新输入。。。")
#     else:
#         print("查无此城市，请重新输入。。。")


# dict={"k1":"v1","k2":"v2","k3":"v3",}
# #1、请循环遍历出所有的key
# for keys in dict.keys():
#     print(keys)
# #2、请循环遍历出所有的value
# for values in dict.values():
#     print(values)
# # 3、请在字典中增加一个键值对,"k4":"v4"
# dict["k4"]="v4"
# print(dict)

'''
小明去超市购买水果
'''
# tips={"苹果":"32.8","香蕉":"22","葡萄":"15.5"}
# fruit=input("请输入水果名称：")
# if fruit=='苹果':
#     print(tips[fruit])
# elif fruit=='香蕉':
#     print(tips[fruit])
# elif fruit=='葡萄':
#     print(tips[fruit])
# else:
#     print("您没有购买该水果。。。")

'''
小明，小刚去超市里购买水果
'''
# fruits={'苹果':12.3,'草莓':4.5,'香蕉':6.3,'葡萄':5.8,'橘子':6.4,'樱桃':15.8}
# info={
#     '小明':{'fruits':{'苹果':4,'草莓':13,'香蕉':10},'money':0.0},
#     '小刚':{'fruits':{'葡萄':19,'橘子':12,'樱桃':30},'money':0.0}
#       }
# money1=fruits['苹果']*info['小明']['fruits']['苹果']+fruits['草莓']*info['小明']['fruits']['草莓']+fruits['香蕉']*info['小明']['fruits']['香蕉']
# money2=fruits['葡萄']*info['小刚']['fruits']['葡萄']+fruits['橘子']*info['小刚']['fruits']['橘子']+fruits['樱桃']*info['小刚']['fruits']['樱桃']
# info['小明']['money']=money1
# info['小刚']['money']=money2
# print(info)

'''
编写一个函数，传入一个列表，并统计每个数字出现的次数
'''
ls=[1,1,1,2,3,2,4,3,3,6,5,5,4]
# def cnt(list):
#     s=set(list)
#     dic={}
#     for i in s:
#         dic[i]=list.count(i)
#     return dic
# print(cnt(ls))

# def cnt(lst):
#     dic={}
#     for i in lst:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]+=1
#     return dic
# print(cnt(ls))


