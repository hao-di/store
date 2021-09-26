'''
    unittest：单元测试框架。
    1.子类继承TestCase
    2.写测试用例,testXxx
    3.运行

'''
from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testAdd1(self):
        num1 = 10
        num2 = 10
        sum = 20

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testAdd2(self):
        num1 = -10
        num2 = -10
        sum = -21

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testAdd3(self):
        num1 = -10
        num2 = 10
        sum = 0

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testAdd4(self):

        num1 = 100000000000000000000000000000000000000000000000000000
        num2 = 10
        sum = 100000000000000000000000000000000000000000000000000010

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)









