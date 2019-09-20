import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
logger = Logger(logger='element-exist').getlog()
logger.setLevel(level=logging.INFO)


class ElemnetExist(SeleniumDriver):
    """
    说明：
        页面通用方法，判断页面元素是否存在,如果不存在，截图保存
        参数：定位方式和元素位置

    """
    def is_element_exist(self,locator,locatorType='id'):
        flag = False
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located((locatorType, locator)))
            logger.info("找到该元素")
            flag = True
        except TimeoutException as e:
            logger.info("在10s内无法定位到该元素，该元素不存在")
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('../errormg/%s.png' % nowtime)
        return flag
