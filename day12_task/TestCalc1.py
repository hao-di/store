'''
    unittest：单元测试框架。
    1.子类继承TestCase
    2.写测试用例,testXxx
    3.运行

'''
from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testMinus1(self):
        num1 = 10
        num2 = 10
        sum = 0

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testMinus2(self):
        num1 = -10
        num2 = -10
        sum = 0

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMinus3(self):
        num1 = -10
        num2 = 10
        sum = -20

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMinus4(self):

        num1 = -10
        num2 = -20
        sum = 10

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMinus5(self):

        num1 = 20
        num2 = -10
        sum = 10

        calc = Calc()
        s = calc.minus(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)








