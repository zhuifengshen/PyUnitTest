#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 17-10-10
import unittest

from samples.mathfunc import add, minus, multi, divide

__author__ = 'Devin -- http://zhangchuzhao.site'
"""
一、unittest的核心概念：test case, test suite, test runner, test fixture
1、一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。
元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
2、多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
3、TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。
4、TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。 测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
5、对一个测试用例环境的搭建和销毁，是一个fixture。

二、unittest的核心流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，
我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。

三、知识点
1、setUp() 和 tearDown() 两个方法（其实是重写了TestCase的这两个方法），这两个方法在每个测试方法执行前以及执行后执行一次，setUp用来为测试准备环境，tearDown用来清理环境
2、如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用 setUpClass() 与 tearDownClass()
3、skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)
skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过
"""


class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""

    @classmethod
    def setUpClass(cls):
        print('this setUpClass() method only called once...')

    @classmethod
    def tearDownClass(cls):
        print('this tearDownClass() method only called once...')

    def setUp(self):
        print('do something before every testcase: prepare environment...')

    def tearDown(self):
        print('do something after every testcase: clean up...')

    def test_add(self):
        """Test method add(a, b)"""
        print('test_add()')
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print('test_minus()')
        self.assertEqual(1, minus(3, 2))

    def test_milti(self):
        """Test method multi(a, b)"""
        print('test_milti()')
        self.assertEqual(6, multi(2, 3))

    # skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过
    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        # self.skipTest('Do not run this')  # TestCase.skipTest()方法也可以跳过
        print('test_divide()')
        self.assertEqual(2, divide(6, 3))
        # self.assertEqual(2, divide(5, 2))  # Expected:2  Actual:2.5


if __name__ == "__main__":
    # 默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果.
    # python3.6 -m unittest test_mathfunc.py
    # python3.6 -m unittest discover
    # unittest.defaultTestLoader.discover('./', pattern='test*.py')
    # unittest.defaultTestLoader.discover()
    unittest.main(verbosity=2)
