import logging
import time
from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.ajxx_tb_page import TbAjxxPage
from pages.ajxx_whsy_page import WshyAjxxPage
from pages.ajxx_ycjy_page import YcjyAjxxPage
from pages.ajxx_ys_page import YsAjxxPage

logger = Logger(logger='ChooseQzcs').getlog()
logger.setLevel(level=logging.INFO)


class StartYw(SeleniumDriver):
    """
    案件信息页面，给嫌疑人选择强制措施
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # 发起提捕流程
    def start_tb(self):
        tb = TbAjxxPage()
        self.double_click(tb.subbitbutton(), 'xpath')
        time.sleep(15)

    # 发起移诉流程
    def start_ys(self):
        ys = YsAjxxPage()
        self.click(ys.subbitbutton(), 'xpath')  # 点击移诉按钮
        time.sleep(2)
        # 在弹出页面，点击确认按钮
        self.switch_iframe(0)  # 有弹出页面，需要切换iframe
        self.double_click(ys.confirmbutton(), 'id')
        time.sleep(15)

    # 延长羁押发起
    def start_ycjy(self):
        ycjy = YcjyAjxxPage()
        # self.excute_js("arguments[0].scrollIntoView();", ycjy.sendbutton(), 'class')
        self.click(ycjy.sendbutton(), 'class')  # 点击送达看守所按钮

    # 保存延长羁押数据
    def save_ycjy(self):
        ycjy = YcjyAjxxPage()
        self.click(ycjy.savebutton(), 'id')  # 点击送达看守所按钮
        time.sleep(5)

    # 网上换押发起
    def start_wshy(self):
        ycjy = WshyAjxxPage()
        self.click(ycjy.sendbutton(), 'class')  # 点击送达看守所按钮
        time.sleep(5)
