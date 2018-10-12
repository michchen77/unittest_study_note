import unittest

# 定义测试类，父类为unittest.TestCse
# 可继承unittest.TestCase的方法，如setUp和TearDown方法，不过此方法可以在子类冲洗，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法
class Test(unittest.TestCase):

    # 定义setUp()方法用于测试用例执行前的初始化工作。
    def setUp(self):
        self.number = input('Enter a number')
        self.number = int(self.number)

    # 定义测试用例，以'test_'开头的明明方法
    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number,10,msg='Your input is not 10')

    def test_case2(self):
        print(self.number)
        self.assertEqual(self.number,20,msg='Your input is not 20')

    @unittest.skip('暂时跳过test_case3')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number,30,msg='Your input is not 30')

    # 定义tearDown()方法用于测试用例执行之后的善后工作。
    def tearDown(self):
        print('Test over')


# 运行
if __name__ == '__main__':
    unittest.main()

'''
# plan B
# 先构造测试集
    # 实例化测试套件
    suite = unittest.TestSuite()

    # 将测试用例加载到测试套件中。
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))

    # 执行
    runner = unittest.TextTestRunner()
    # 使用run()方法运行测试套件
    runner.run(suite)
'''

'''
# plan c
    # 构造测试集
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # 执行
    runner = unittest.TextTestRunner()
    runner.run(discover)
'''