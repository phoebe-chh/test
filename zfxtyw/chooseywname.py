import logging
from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.home_page import HomePage

logger = Logger(logger='chooseywlx').getlog()
logger.setLevel(level=logging.INFO)


class ChooseXtName(SeleniumDriver):
    """
    选择进入的协同名称
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # 提捕流程
    def choose_tb(self):
        ywlx = HomePage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ywlx.tbyw(), 'xpath')  # 选择业务类型

    # 移诉流程
    def choose_ys(self):
        ywlx = HomePage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ywlx.ysyw(), 'xpath')  # 选择业务类型

    # 延长羁押流程
    def choose_ycjy(self):
        ywlx = HomePage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ywlx.ycjy(), 'xpath')  # 选择业务类型

    # 延长羁押流程
    def choose_kss_ycjy(self):
        ywlx = HomePage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ywlx.ycjy_kss(), 'xpath')  # 选择业务类型

    # 换押流程
    def choose_wshy(self):
        ywlx = HomePage()  # 实例化页面，获取元素，对元素进行操作
        self.click(ywlx.wshy(), 'xpath')  # 选择业务类型
