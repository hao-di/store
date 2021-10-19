# -*- coding: utf-8 -*-
# @Time : 2021/10/18 13:09
# @Author : 小菜鸡儿
from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import InitPage
from LoginOperation import LoginOpera
import time

@ddt
class TestLogin(TestCase):
    #在所有方法执行前执行
    def setUp(self) -> None:
        url='127.0.0.1:4723/wd/hub'

        param={
            "platformName":"Android",
            "platformVersion":"7.1.2",
            "deviceName":"127.0.0.1:62001",
            "appPackage":"com.sina.weibo",
            "appActivity":"com.sina.weibo.SplashActivity"
        }
        #连接手机和app
        self.driver=webdriver.Remote(url,param)
        #等待app启动
        time.sleep(5)

    #在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  #退出app

    @data(*InitPage.login_success_data)
    def testSuccessCase(self,testdata):
        #提取数据
        username=testdata["username"]
        password=testdata["password"]
        expect=testdata["expect"]
        #调用被测操作类
        loginObj=LoginOpera(self.driver)
        #调用被测方法
        loginObj.login(username,password)
        #获取实际结果
        data=loginObj.getSuccessResult()
        #断言
        if data!=expect:
            self.driver.save_screenshot('error.jpg')
        else:
            self.assertEqual(data,expect)

    @data(*InitPage.login_error_data)
    def testErrorCase(self,testdata):
        #提取数据
        username=testdata["username"]
        password=testdata["password"]
        expect=testdata["expect"]
        #调用被测操作类
        loginObj=LoginOpera(self.driver)
        loginObj.login(username,password)
        #获取实际结果
        data=loginObj.getErrorResult()
        #断言
        self.assertEqual(data,expect)






