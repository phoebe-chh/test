import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='login-page-element').getlog()
logger.setLevel(level=logging.INFO)


class LoginPage(ReadExcel):
    '''
    说明：
        通过pagename和elementname获取配置文件中的信息
    '''
    def username_textbox(self):
        return self.get_element('login_page','element1')

    def password_textbox(self):
        return self.get_element('login_page', 'element2')

    def login_button(self):
        return self.get_element('login_page', 'element3')
