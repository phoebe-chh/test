import logging

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.login_page import LoginPage

logger = Logger(logger='LoginPage').getlog()
logger.setLevel(level = logging.INFO)


class LoginPageTest(SeleniumDriver):
    """
    登录页面的操作，填写用户名，密码,点击登录按钮
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def login(self):
        loginpage = LoginPage()  # 实例化页面，获取元素，对元素进行操作
        self.text_input('241808', loginpage.username_textbox())  # 输入用户名
        self.text_input('123', loginpage.password_textbox())  # 输入密码
        self.click(loginpage.login_button(), 'class')  # 点击登录按钮

