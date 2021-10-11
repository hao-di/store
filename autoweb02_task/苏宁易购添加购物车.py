# -*- coding: utf-8 -*-
# @Time : 2021/10/9 17:12
# @Author : 小菜鸡儿
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r'https://www.suning.com/')
driver.maximize_window()
#收缩商品
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys('thinkpad')
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
#选择商品
driver.find_element_by_xpath("//*[@id='0070998547-12189746515']/div/div/div[1]/div/a/img").click()
data=driver.window_handles
driver.switch_to.window(data[1])
#添加购物车并结算
driver.find_element_by_xpath("//*[@id='addCart']").click()
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()
driver.quit()
