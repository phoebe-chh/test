import logging
import time

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.ajxx_tb_page import TbAjxxPage
from pages.ajxx_ys_page import YsAjxxPage

logger = Logger(logger='ChooseQzcs').getlog()
logger.setLevel(level = logging.INFO)


class ChooseQzcs(SeleniumDriver):
    """
    案件信息页面，给嫌疑人选择强制措施
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def chooseqzcs_tb(self):
        tb=TbAjxxPage()  # 实例化页面，获取元素，对元素进行操作
        self.double_click(tb.qzcscell(), 'xpath')  # 点击强制措施所在表格
        self.double_click(tb.qzscbutton(), 'css')  # 点击强制措施编辑按钮
        self.double_click(tb.qzsclist(), 'xpath')  # 点击下拉框
        self.double_click(tb.qzscfirst(), 'xpath')  # 选择第一个强制措施
        self.double_click(tb.qzscconfirebutton(), 'xpath')  # 勾选强制措施勾选框
        self.double_click(tb.savebutton(), 'xpath')  # 点击保存按钮
        time.sleep(2)

    def chooseqzcs_ys(self):
        tb=YsAjxxPage()  # 实例化页面，获取元素，对元素进行操作
        time.sleep(5)
        logger.info("开始执行js")
        self.excute_js("arguments[0].scrollIntoView();",tb.qzcscell(),'xpath')  # 执行js脚本，把滚动条移动到底部
        time.sleep(5)
        self.double_click(tb.qzcscell(), 'xpath')  # 点击强制措施所在表格
        self.double_click(tb.qzscbutton(), 'css')  # 点击强制措施编辑按钮
        self.double_click(tb.qzsclist(), 'xpath')  # 点击下拉框
        self.double_click(tb.qzscfirst(), 'xpath')  # 选择第一个强制措施
        self.double_click(tb.qzscconfirebutton(), 'xpath')  # 勾选强制措施勾选框
        self.double_click(tb.savebutton(), 'xpath')  # 点击保存按钮
        time.sleep(2)



