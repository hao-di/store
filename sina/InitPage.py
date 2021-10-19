# -*- coding: utf-8 -*-
# @Time : 2021/10/18 13:07
# @Author : 小菜鸡儿
'''
    1、数据类：
        只准备数据部分：不参与任何操作
'''
class InitPage:
    login_success_data=[
        # id:com.sina.weibo:id/titleLeft
        {"username":"13453676378","password":"123456","expect":"返回"}
    ]
    login_error_data=[
        # xpath:/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ScrollView/android.widget.TextView
        {"username":"13453676378","password":"123","expect":"登录名或密码错误"},
        {"username":"13552648187","password":"123456","expect":"登录名或密码错误"}
    ]








