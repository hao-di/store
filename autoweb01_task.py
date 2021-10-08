# -*- coding: utf-8 -*-
'''
    任务：
        1：把所有页面操作使用自动化来做。
        2：自动化实现在京东搜索一个商品。
        3：在百度中做搜索操作。
'''
import time
from selenium import webdriver
driver = webdriver.Chrome()

'''输入框'''
# driver.get(r"C:/Users/lenovo/PycharmProjects/proj2/tasks/练习的html/main.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='input1']").send_keys('jason')
# time.sleep(2)
# driver.quit()

'''输入框'''
# driver.get(r"C:/Users/lenovo/PycharmProjects/proj2/tasks/练习的html/frame.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='input1']").send_keys('jason')
# time.sleep(2)
# driver.quit()

'''弹框'''
# driver.get(r'C:/Users/lenovo/PycharmProjects/proj2/tasks/练习的html/弹框的验证/dialogs.html')
# driver.maximize_window()
# # driver.find_element_by_xpath("//*[@id='alert' and @value='alert' and @type='button']").click()
# # driver.switch_to.alert.accept()
# driver.find_element_by_xpath("//*[@id='confirm' and @value='confirm' and @type='button']").click()
# # driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# time.sleep(2)
# driver.quit()


'''跳转'''
# driver.get(r'C:/Users/lenovo/PycharmProjects/proj2/tasks/练习的html/跳转页面/pop.html')
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='goo']").click()
# time.sleep(2)
# driver.quit()

'''上传文件和下拉列表'''
# driver.get(r'C:/Users/lenovo/PycharmProjects/proj2/tasks/练习的html/上传文件和下拉列表/autotest.html')
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@name='account' and @id='accountID' and @type='text']").send_keys('jason')
# driver.find_element_by_xpath("//*[@name='password' and @id='passwordID' and @type='password']").send_keys('123456')
# driver.find_element_by_xpath("//*[@id='areaID']").send_keys('北京市')
# time.sleep(1)
# driver.find_element_by_xpath("//*[@name='u2' and @id='sexID2' and @type='radio']").click()
# driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='spring']").click()
# driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='winter']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r'C:\Users\lenovo\Desktop\cuptest.png')
# driver.find_element_by_xpath("//*[@class='u16' and @id='buttonID' and @type='button' and @value='submit']").click()
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.quit()

'''京东搜索'''
# driver.get(r'https://www.jd.com/')
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@type='text' and @autocomplete='off' and @id='key']").send_keys('电脑')
# driver.find_element_by_xpath("//*[@class='button' and @aria-label='搜索']").click()
# time.sleep(8)
# driver.quit()

'''百度搜索'''
# driver.get(r'https://www.baidu.com/')
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='kw' and @name='wd' and @class='s_ipt']").send_keys('python')
# driver.find_element_by_xpath("//*[@type='submit' and @id='su' and @value='百度一下']").click()
# time.sleep(6)
# driver.quit()