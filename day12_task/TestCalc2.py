'''
    unittest：单元测试框架。
    1.子类继承TestCase
    2.写测试用例,testXxx
    3.运行

'''
from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testMulti1(self):
        num1 = 10
        num2 = 10
        sum = 100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testMulti2(self):
        num1 = -10
        num2 = -10
        sum = 100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti3(self):
        num1 = -10
        num2 = 10
        sum = -100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti4(self):

        num1 = 100000000000000000000000000000000000000000000000000000
        num2 = 10
        sum = 1000000000000000000000000000000000000000000000000000000

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti5(self):

        num1 = 10
        num2 = 0
        sum = 0

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)







