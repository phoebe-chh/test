import unittest

from base.browser_driver import BrowserDriver
from pages.login_page import LoginPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'ga') # 选择公安或者政法端进行登录

    def test_01_fill_(self):
        '''登陆公安端，查看页面展示和数据库中字段是否对应'''
        loginpage = LoginPage(self.driver)
        loginpage.login(241808,123)  # 输入用户名和密码
        result=loginpage.is_login_sucess("苏州市吴江区公安局")
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)

