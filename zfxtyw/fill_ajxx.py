import logging

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.ajxx_tb_page import TbAjxxPage


logger = Logger(logger='fillvalueoftb').getlog()
logger.setLevel(level = logging.INFO)


class FillElementValue(SeleniumDriver):
    """
    案件信息页面，在案件信息中填写文书文号等字段内容
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def fill_in_tb_ajxx(self):
        tb=TbAjxxPage()  # 实例化案件信息页面，给文本框输入数据
        self.text_input('10',tb.wpjsinputbox(),'id')  # 给物品件数赋值
        self.text_input('[文书]11111111111', tb.wswhinputbox(), 'id')  # 给文书文号赋值


