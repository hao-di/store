# -*- coding: utf-8 -*-
# @Time : 2021/10/11 9:50
# @Author : 小菜鸡儿
import time
from selenium import webdriver
class Register(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get(r'http://localhost:8080/HKR/')
        self.driver.maximize_window()
    #用户注册
    def reUser(self):
        #第一步
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys("summer")
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("小精豆")
        self.driver.find_element_by_xpath("//*[@id='pwd']").send_keys("1234562")
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
        #第二步
        self.driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("66")
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]/option[1]").click()
        self.driver.find_element_by_xpath("//*[@id='classname']/option[3]").click()
        self.driver.find_element_by_xpath("/html/body/form/fieldset[2]/input[3]").click()
        #等待两秒,至下一步按钮不被遮挡
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
        #第三步
        self.driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("123356@qq.com")
        self.driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("13235735621")
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("老牛湾儿")
        self.driver.find_element_by_xpath("//*[@id='btn_reg']").click()
        #等待弹出注册成功的信息
        time.sleep(2)
        #点击注册成功的确定按钮
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/a/span").click()
    #关闭浏览器
    def quit(self):
        self.driver.quit()

if __name__=='__main__':
    u=Register()
    u.reUser()
    u.quit()

