# -*- coding: utf-8 -*-
# @Time : 2021/10/18 13:09
# @Author : 小菜鸡儿
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

#加载测试用例
tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")
#创建运行器
runner=HTMLTestRunner.HTMLTestRunner(
    #标题
    title="新浪微博app测试报告",
    #子标题
    description="登录测试",
    #详细程度
    verbosity=1,
    #保存
    stream=open(file='新浪微博app登录测试报告.html',mode='w+',encoding='utf-8')
)
#运行测试用例
runner.run(tests)