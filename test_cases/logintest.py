import unittest
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
import logging
from common.logger import Logger
from zfxtyw.login import LoginPageTest
logger = Logger(logger='logintest').getlog()
logger.setLevel(level=logging.INFO)


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'ga')  # 选择公安或者政法端进行登录,浏览器的选择在ini文件中进行配置

    def test_01_login(self):
        """登陆"""
        loginpage = LoginPageTest(self.driver)
        loginpage.login()  # 使用登陆方法
        # dw = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        # result = dw.is_element_exist('//*[@id="identify"]',"xpath")  # 通过登陆后的单位判断是否登陆成功
        # self.assertTrue(result)
        # raise AssertionError("测试失败")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # 运行所有
    # unittest.main(verbosity=2)
    # 运行单个用例
    testunit=unittest.TestSuite()
    testunit.addTest(LoginTest('test_01_login'))  # 添加测试用例方法名
    runer=unittest.TextTestRunner(verbosity=2)
    runer.run(testunit)
    #



