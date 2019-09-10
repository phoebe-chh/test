import logging
import time

from base.selenium_driver import SeleniumDriver
from logs.logger import Logger

from pages.yw_list_tb import TbYwListPage

logger = Logger(logger='addtbaj').getlog()
logger.setLevel(level = logging.INFO)


class AddTbAJ(SeleniumDriver):
    """
    提捕案件列表的操作，点击添加案件按钮
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def addtbaj(self):
        tb=TbYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.click(tb.addbutton(),'class')  # 点击添加案件按钮



