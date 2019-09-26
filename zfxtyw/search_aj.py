import logging
import time

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.yw_list_tb import TbYwListPage
from pages.yw_list_wshy import WshyYwListPage
from pages.yw_list_ycjy import YcjyYwListPage
from pages.yw_list_ys import YsYwListPage

logger = Logger(logger='search-aj').getlog()
logger.setLevel(level=logging.INFO)


class SearchAJ(SeleniumDriver):
    """
    业务列表中查询信息
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # 提捕列表中查询案件
    def search_tbxyrxm(self, xyrxm):
        tb = TbYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.text_input(xyrxm, tb.xyrxminputtext(), 'xpath')  # 点击添加案件按钮
        self.click(tb.searchbutton(), 'id')
        time.sleep(5)

    # 移诉列表中查询案件
    def search_ysxyrxm(self, xyrxm):
        tb = YsYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.text_input(xyrxm, tb.xyrxminputtext(), 'id')  # 点击添加案件按钮
        self.click(tb.searchbutton(), 'id')
        time.sleep(5)

    # 延长羁押列表中查询案件
    def search_ycjy(self, xyrxm):
        tb = YcjyYwListPage()  # 实例化页面，获取元素，对元素进行操作
        self.text_input(xyrxm, tb.xyrtext(), 'id')  # 点击添加案件按钮
        self.click(tb.searchbutton(), 'id')
        time.sleep(5)
