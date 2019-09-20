import logging

from base.selenium_driver import SeleniumDriver
from common.logger import Logger

from pages.yw_list_tb import TbYwListPage
from pages.yw_list_wshy import WshyYwListPage
from pages.yw_list_ycjy import YcjyYwListPage

logger = Logger(logger='addtbaj').getlog()
logger.setLevel(level = logging.INFO)


class AddAJ(SeleniumDriver):
    """
    业务列表中添加案件类，不同业务方法不同
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # 添加提捕案件
    def add_tb_aj(self):
        tb=TbYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.click(tb.addbutton(),'class')  # 点击添加案件按钮

    # 添加延长羁押案件
    def add_ycjy_aj(self):
        ycjy=YcjyYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ycjy.addbutton(),'class')  # 点击添加案件按钮

    # 添加网上换押案件
    def add_wshy_aj(self):
        ycjy=WshyYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ycjy.addbutton(),'class')  # 点击添加案件按钮




