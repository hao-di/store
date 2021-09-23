# -*- coding: utf-8 -*-
# @Time : 2021/9/23 13:09
# @Author : 小菜鸡儿
# @FileName: exp.py
# @Software: PyCharm

import xlrd

# 打开工作簿
wb = xlrd.open_workbook(filename="./2020年每个月的销售情况.xlsx",encoding_override=True)

'''
    存储结构：
        风衣：{
            "sum_money":xxxx,  # 总销售额
            "sum_count":xxx,   # 总销售量
        },
        "羽绒服":{
            "sum_money":xxx,
            "sum_count":xxxxx,    
        }
'''

class Sell:
    def allData(self,*nsheet):
        store = {}
        # 现在要获取所有工作簿的表格数据
        for i in nsheet: # 遍历每个选项卡
            # 获取第n个选项卡
            st = wb.sheet_by_index(i)
            # 获取有多少行
            nrow = st.nrows
            for j in range(1,nrow):  # 遍历选项卡每一行
                cell = st.row_values(j) # 获取第j行数据
                if cell[1] in store:  # 判断在存储库是否存在
                    store[cell[1]]={   # 若存在，则累加数据
                        "sum_money":round(store[cell[1]]["sum_money"] + cell[2] * cell[4],2),
                        "sum_count":int(store[cell[1]]["sum_count"] + cell[4])
                    }
                else:  # 若不存在，这是以第一次统计数据
                    store[cell[1]] = {
                        "sum_money":round(cell[2] * cell[4],2),
                        "sum_count":int(cell[4])
                    }
        return store
    def popular(self,store,season):
        for cloth in store:
            if store[cloth]['sum_count']==max(store[item]["sum_count"] for item in store):
                print(season+'最畅销的衣服是：',cloth)
            elif store[cloth]['sum_count']==min(store[item]["sum_count"] for item in store):
                print(season+'销量最低的衣服是：', cloth)
if __name__=='__main__':
    sp=Sell()
    springdata=sp.allData(1,2,3)
    sp.popular(springdata,'春季')
    print("------------------------------------------")
    su=Sell()
    summerdata=su.allData(4,5,6)
    su.popular(summerdata,'夏季')
    print("------------------------------------------")
    au=Sell()
    autumndata=au.allData(7,8,9)
    au.popular(autumndata,'秋季')
    print("------------------------------------------")
    wi=Sell()
    winterdata=wi.allData(10,11,0)
    wi.popular(winterdata,'冬季')

