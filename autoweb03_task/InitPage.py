'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import xlrd
import pymysql
'''xlrd参数化'''
# class InitPage:
#     def readData(self):
#         wb = xlrd.open_workbook(filename=r"./HKR.xlsx", encoding_override="utf-8")
#         st = wb.sheet_by_name('Login')
#         rows = st.nrows
#         da=[]
#         for i in range(1,rows):
#             # print(st.row_values(i))
#             da.append(st.row_values(i))
#         #[['jason', '1234567', 'Student Login'], ['不再爱了', '1234567', 'Student Login'], ['jason1213123123123', '1234567', '账户名错误或密码错误!别瞎弄!'], ['不再爱了', '123456789898945', '账户名错误或密码错误!别瞎弄!']]
#         return da
'''mysql参数化'''
class InitPage:
    def readData(self):
        con=pymysql.connect(host='localhost',user='root',password='root',database='login')
        cur=con.cursor()
        sql='select * from user'
        cur.execute(sql)
        con.commit()
        da=cur.fetchall()
        cur.close()
        con.close()
        #(('jason', '1234567', 'Student Login'), ('不再爱了', '1234567', 'Student Login'), ('jason1213123123123', '1234567', '账户名错误或密码错误!别瞎弄!'), ('不再爱了', '123456789898945', '账户名错误或密码错误!别瞎弄!'))
        return da
