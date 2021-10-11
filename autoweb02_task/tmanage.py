# -*- coding: utf-8 -*-
# @Time : 2021/10/11 10:24
# @Author : 小菜鸡儿
import time
from selenium import webdriver
class Tmanage(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(r'http://localhost:8080/HKR/')
        self.driver.maximize_window()
    def login(self):
        #教师登录
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys("qiaoyueyang")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
    def mTeacher(self):
        #查询
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("佟贺")
        self.driver.find_element_by_xpath("//*[@id='search_user']/span").click()
        #重置密码
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()
        self.driver.switch_to.alert.accept()
    def mStudent(self):
        #查询
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("胡莹")
        self.driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("13245638767")
        self.driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()
        #设置毕业状态(设置后毕业状态仍未改变)
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[11]/div/a").click()
        self.driver.find_element_by_xpath("/html/body/div[9]/div[3]/a").click()
    def mCourse(self):
        #添加课程
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span").click()
        #清空输入框并赋值
        self.driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").clear().send_keys("OpenCV")
        self.driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").clear().send_keys("计算机视觉")
        self.driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[1]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[12]/div[3]/a").click()
        #取消添加
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span").click()
        #清空输入框并重新赋值
        self.driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").clear().send_keys("经典阅读")
        self.driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").clear().send_keys("感受经典,传承文化")
        self.driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span/span[1]").click()
        time.sleep(2)
    def response(self):
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_15']").click()
        time.sleep(2)
        #查询评价(当日有评价)
        self.driver.find_element_by_xpath("//*[@id='J-xl']").click()
        time.sleep(2)
        #2021-10-11
        self.driver.find_element_by_xpath("//*[@id='laydate_table']/tbody/tr[3]/td[2]").click()
        time.sleep(2)

        #导出当前评价
        self.driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()

        #查看评价报表
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_16']").click()
        time.sleep(2)
    def his_log(self):
        '''刷新当前页面'''
        self.driver.refresh()
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_18']/span[4]/a").click()
        time.sleep(2)
        # 查询今日操作日志
        self.driver.find_element_by_xpath("//*[@id='J-history']").click()
        time.sleep(2)
        '''直接选择日期弹窗显示不出,崩溃报错;需重新刷新页面后再次执行操作'''
        self.driver.find_element_by_xpath("//*[@id='laydate_today']").click()
        #设置分页显示数据量，第xx页模块
        self.driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[1]/select/option[5]").click()
        self.driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]").click()
        time.sleep(2)
        #点击查询
        self.driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[2]/a/span").click()
        '''需点两次查询,要不然数据未刷新出来'''
        self.driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[2]/a/span").click()
        time.sleep(2)
        #导出当前日志
        self.driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()
        time.sleep(2)
    #关闭浏览器
    def quit(self):
        self.driver.quit()

if __name__=="__main__":
    t=Tmanage()
    t.login()
    t.mTeacher()
    t.mStudent()
    t.mCourse()
    t.response()
    t.his_log()
    t.quit()
