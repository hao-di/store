# -*- coding: utf-8 -*-
# @Time : 2021/10/11 11:34
# @Author : 小菜鸡儿
import time
from selenium import webdriver
class commonUser(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(r'http://localhost:8080/HKR/')
        self.driver.maximize_window()
    def login(self):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys("huying")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
    def alterPicture(self):
        #修改头像
        self.driver.find_element_by_xpath("//*[@id='img']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='ul_pic']/li[8]/img").click()
        time.sleep(2)
        #上传头像
        self.driver.find_element_by_xpath("//*[@id='file1']").send_keys(r"C:\Users\lenovo\PycharmProjects\proj2\tasks\autoweb02_task\pig.png")
        self.driver.find_element_by_xpath("//*[@id='pic_btn']").click()
        time.sleep(2)
        #提交今日评价
        self.driver.refresh()
        self.driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select/option[2]").click()
        self.driver.find_element_by_xpath("//*[@id='tea_td']/select/option[4]").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[1]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[3]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='textarea']").send_keys("无")
        self.driver.find_element_by_xpath("//*[@id='subtn']").click()
        self.driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()
    #修改个人信息
    def alterInfo(self):
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
        time.sleep(2)
        #清空输入框
        self.driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
        #重新赋值
        self.driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("34")
        self.driver.find_element_by_xpath("//*[@id='btn_modify']").click()
        time.sleep(2)
    #查询所有好友
    def inquire(self):
        self.driver.find_element_by_xpath("//*[@id='_easyui_tree_10']").click()
        time.sleep(2)
    #退出
    def logout(self):
        self.driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
        time.sleep(2)
    #关闭浏览器
    def quit(self):
        self.driver.quit()

if __name__=='__main__':
    cu=commonUser()
    cu.login()
    cu.alterPicture()
    cu.alterInfo()
    cu.inquire()
    cu.logout()
    cu.quit()