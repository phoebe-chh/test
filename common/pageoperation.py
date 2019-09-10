import time
from selenium.webdriver.support import expected_conditions as EC
import logging
from base.selenium_driver import SeleniumDriver
from logs.logger import Logger
logger = Logger(logger='pageoperation').getlog()
logger.setLevel(level=logging.INFO)


class PageOperation(SeleniumDriver):

    '''
        说明：
            页面通用方法，切换窗口句柄
            通过页面title，判断是否切换页面成功
    '''
    def switch_window(self,number):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[number])
