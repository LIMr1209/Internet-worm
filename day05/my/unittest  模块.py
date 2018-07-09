import unittest


# 测试的py文件要以字母开头

class MyTest(unittest.TestCase):
    def setUp(self):
        print('开始测试')  # ，测试开始前的代码

    def testTest(self):
        print('测试')    #测试代码 函数名以test开头

    def tearDown(self):
        print('结束测试')  # ，测试结束后的代码


if __name__ == '__main__':
    unittest.main()  #固定调用方法
