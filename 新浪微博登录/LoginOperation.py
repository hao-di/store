# -*- coding: utf-8 -*-
# @Time : 2021/10/18 10:05
# @Author : 小菜鸡儿
'''
    1、登录操作类：
        只有页面登录的操作
'''

import time
class LoginOpera:
    #driver申明一个全局变量
    def __init__(self,driver):
        self.driver=driver  #变成全局的driver对象

    #登录的实际操作
    def login(self,username,password):
        #同意用户协议
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
        #等待页面加载出来
        time.sleep(10)
        #点击登录
        self.driver.find_element_by_id("com.sina.weibo:id/titleBack").click()
        time.sleep(5)
        #切换短信密码登录
        self.driver.find_element_by_id("com.sina.weibo:id/iv_psw").click()
        time.sleep(5)
        #输入手机号或邮箱
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname").send_keys(username)
        #输入密码
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw").send_keys(password)
        #勾选同意用户协议
        self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
        #点击登录
        self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw").click()
        time.sleep(30)

    #获取登录成功的实际结果
    def getSuccessResult(self):
        data=self.driver.find_element_by_id("com.sina.weibo:id/titleLeft").text
        return data

    #获取登录失败的实际结果
    def getErrorResult(self):
        data=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ScrollView/android.widget.TextView").text
        return data
