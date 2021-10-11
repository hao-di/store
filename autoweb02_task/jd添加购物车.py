# -*- coding: utf-8 -*-
# @Time : 2021/10/9 15:02
# @Author : 小菜鸡儿
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r'https://www.jd.com/')
driver.maximize_window()
#搜索商品
driver.find_element_by_xpath("//*[@id='key']").send_keys('thinkpad e580')
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
#选择商品
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
data=driver.window_handles
driver.switch_to.window(data[1])
#加入购物车
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
#选择账户登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
#输入用户名密码点击登录
driver.find_element_by_xpath("//*[@id='loginname']").send_keys('账号')
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys('密码')
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
#等待几秒,以便手动拖动滑块验证
time.sleep(5)
#关闭浏览器
driver.quit()
