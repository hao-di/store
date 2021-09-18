'''
    xlrd:读取
    xlwt:写入
    xlrd:0.9.3版本
    xlwt:

    python -m  pip install   xlrd==0.9.3

    1.步骤
    1.打开工作簿
    2.找到你想操作的选项卡
    3.通过坐标读取数据
任务1：
    把2020年的所有数据统计分析并打印出来
        全年的销售总额
        每件衣服的销售（件数）占比 (全年)
        每件衣服的月销售占比 (全年)
        每件衣服的销售额占比 (全年)

        最畅销的衣服是那种
        每个季度最畅销的衣服 (2-4;5-7;8-10;11-1)
        全年销量最低的衣服
任务2：
    把excel表的所有数据存储到数据库。
任务3：
    将三国集团数据，导出到excel里。
'''
import xlrd
import xlwt
import pymysql

#1.打开
wb = xlrd.open_workbook(filename=r"./2020年每个月的销售情况.xlsx")

# 2.操作选项卡
# sheet = wb.sheet_by_name("1月")
'''全年的销售总额'''
# sum = 0
# for i in range(0,12):
#     sheet = wb.sheet_by_index(i)
#     cols = sheet.ncols  # 获取有多少列
#     rows = sheet.nrows # 获取有多少行
#     for j in range(1,rows):
#         data = sheet.row_values(j)
#         sum = sum + data[2] * data[4]
# print("销售总额：￥",round(sum,2))
'''每件衣服的销售（件数）占比 (全年)'''
# ls=[]
# dic={}
# n=0
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     cloths=sheet.col_values(1)
#     n=n+(len(cloths)-1)
#     for j in range(1,rows):
#         data=sheet.cell_value(j,1)
#         ls.append(data)
# # print(ls)
# s=set(ls)
# for k in s:
#     dic[k]=ls.count(k)
# print(dic)
# # print(n)
# for keys in dic:
#     print("%s的年销售占比为：%.2f"%(keys,dic[keys]/n))
'''每件衣服的月销售占比 (全年)'''
# ls=[]
# dic={}
# n=0
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     cloths=sheet.col_values(1)
#     n=n+(len(cloths)-1)
# print(n)
# # print(ls)
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     for j in range(1,rows):
#         data=sheet.cell_value(j,1)
#         ls.append(data)
#     s=set(ls)
#     for k in s:
#         dic[k]=ls.count(k)
#     print(dic)
#     # print(n)
#     for keys in dic:
#         print("%s的%d月销售占比为：%f"%(keys,i+1,dic[keys]/n))
#     ls.clear()
#     dic.clear()
#     s.clear()
'''每件衣服的销售额占比 (全年)'''
# sum = 0
# for i in range(0,12):
#     sheet = wb.sheet_by_index(i)
#     rows = sheet.nrows # 获取有多少行
#     for j in range(1,rows):
#         data = sheet.row_values(j)
#         sum = sum + data[2] * data[4]
# print("销售总额：￥",round(sum,2))
#
# ls=[]
# dic={}
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     for j in range(1,rows):
#         data=sheet.row_values(j)
#         ls.append(data[1])
# # print(ls)
#         s=set(ls)
#         for k in s:
#             if k==sheet.cell_value(j,1):
#                 dic[k]=ls.count(k)*data[2]
# print(dic)
# for keys in dic:
#     print("%s的销售额占比为：%f"%(keys,dic[keys]/sum))
'''最畅销的衣服是那种'''
# ls=[]
# dic={}
# n=0
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     cloths=sheet.col_values(1)
#     n=n+(len(cloths)-1)
#     for j in range(1,rows):
#         data=sheet.cell_value(j,1)
#         ls.append(data)
# # print(ls)
# s=set(ls)
# for k in s:
#     dic[k]=ls.count(k)
# print(dic)
# # print(n)
# for keys in dic:
#     if dic[keys]==max(dic.values()):
#         print("最畅销的衣服是：%s"%(keys))
'''每个季度最畅销的衣服'''
# spring=['2月','3月','4月']
# summer=['5月','6月','7月']
# autumn=['8月','9月','10月']
# winter=['11月','12月','1月']
# def popular(season):
#     ls=[]
#     dic={}
#     n=0
#     for i in season:
#         sheet=wb.sheet_by_name(i)
#         rows=sheet.nrows
#         cloths=sheet.col_values(1)
#         n=n+(len(cloths)-1)
#         for j in range(1,rows):
#             data=sheet.cell_value(j,1)
#             ls.append(data)
#     # print(ls)
#     s=set(ls)
#     for k in s:
#         dic[k]=ls.count(k)
#     print(dic)
#     # print(n)
#     for keys in dic:
#         if dic[keys]==max(dic.values()):
#             return keys
# info='''
#      春季最畅销的衣服是：%s
#      夏季最畅销的衣服是：%s
#      秋季最畅销的衣服是：%s
#      冬季最畅销的衣服是：%s
#      '''
# print(info%(popular(spring),popular(summer),popular(autumn),popular(winter)))
'''全年销量最低的衣服'''
# ls=[]
# dic={}
# n=0
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     cloths=sheet.col_values(1)
#     n=n+(len(cloths)-1)
#     for j in range(1,rows):
#         data=sheet.cell_value(j,1)
#         ls.append(data)
# # print(ls)
# s=set(ls)
# for k in s:
#     dic[k]=ls.count(k)
# print(dic)
# # print(n)
# for keys in dic:
#     if dic[keys]==min(dic.values()):
#         print("全年销量最低的衣服是：%s"%(keys))
'''把excel表的所有数据存储到数据库'''
# ls=[]
# con=pymysql.connect(host="localhost",user="root",password="123456",database="market")
# cursor = con.cursor()
# for i in range (0,12):
#     sheet=wb.sheet_by_index(i)
#     rows=sheet.nrows
#     cols=sheet.ncols
#     for m in range(1,rows):
#         for n in range(0,cols):
#             data=sheet.cell_value(m,n)
#             ls.append(data)
#         print(ls)
#         # print(str(i+1)+'月'+ls[0])
#         sql="insert into sell(日期,服装名称,单价,本月库存数量,日销售量) values(%s,%s,%s,%s,%s)"
#         param=[str(i+1)+'月'+ls[0],ls[1],ls[2],ls[3],ls[4]]
#         cursor.execute(sql, param)
#         ls.clear()
# con.commit()
# cursor.close()
# con.close()
'''将三国集团数据，导出到excel里'''
def export_excel(table_name):
    fileds=[]
    conn = pymysql.connect(host="localhost",user="root",password="123456",database="company")
    cursor = conn.cursor()
    sql = "select * from %s"%table_name
    # 读取数据
    cursor.execute(sql)
    # fileds = [filed[0] for filed in cursor.description]
    for i in cursor.description:
        # print(i)
        fileds.append(i[0])
    # print(fileds)

    all_date = cursor.fetchall() #获取所有数据
    for result in all_date:
        print(result)
    #写excel
    book = xlwt.Workbook(encoding='utf-8') #创建一个book
    sheet = book.add_sheet('result',cell_overwrite_ok=True) #创建一个sheet表
    for col,filed in enumerate(fileds): #获取值及下标
        # print(col,filed)
        sheet.write(0,col,filed)  #写入表头
    #从第一行开始写入数据
    row = 1
    for data in all_date:
        for col,filed in enumerate(data):
            sheet.write(row,col,filed)
        row += 1
    book.save('%s.xls' %table_name)

if __name__ == '__main__':
    export_excel('t_employees')
    export_excel('t_dept')

