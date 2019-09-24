import unittest
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
from zfxtyw.login import LoginPageTest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        # 选择公安或者政法端进行登录
        cls.driver = browser.open_browser(browser, 'zf')

    def test_01_login_zfxt_ga(self):
        """登陆政法端，查看页面展示和数据库中字段是否对应"""
        loginpage = LoginPageTest(self.driver)
        loginpage.login()  # 使用登陆方法
        po = ElemnetExist(self.driver)
        result=po.is_element_exist('//*[@id="identify"]',"xpath")  # 通过登陆后的单位判断是否登陆成功
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



