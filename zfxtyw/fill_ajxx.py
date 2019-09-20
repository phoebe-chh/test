import logging

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.ajxx_tb_page import TbAjxxPage
from pages.ajxx_ycjy_page import YcjyAjxxPage

logger = Logger(logger='fillvalueoftb').getlog()
logger.setLevel(level = logging.INFO)


class FillElementValue(SeleniumDriver):
    """
    案件信息页面，在案件信息中填写文书文号等字段内容
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # 提捕页面填写数据
    def fill_in_tb_ajxx(self):
        tb=TbAjxxPage()  # 实例化案件信息页面，给文本框输入数据
        self.text_input('10',tb.wpjsinputbox(),'id')  # 给物品件数赋值
        self.text_input('[文书]11111111111', tb.wswhinputbox(), 'id')  # 给文书文号赋值

    # 填写延长羁押页面信息
    def fill_ycjy_ajxx(self):
        ycjy=YcjyAjxxPage()  # 实例化案件信息页面，给文本框输入数据
        self.text_input('同案人',ycjy.tarfield())  # 同案人输入框
        js = 'document.getElementById("jqDatedyjyksrq").removeAttribute("readonly")'
        self.driver.execute_script(js)  # 执行js脚本
        self.text_input('2019-09-20', ycjy.ksrq())  # 原羁押开始日期
        js = 'document.getElementById("jqDatedyjyjzrq").removeAttribute("readonly")'
        self.driver.execute_script(js)  # 执行js脚本
        self.text_input('2019-09-21', ycjy.jzrq())  # 原羁押截止日期

    # 填写网上换押页面信息
    def fill_wshy_ajxx(self):
        ycjy = YcjyAjxxPage()  # 实例化案件信息页面，给文本框输入数据
        self.text_input('同案人', ycjy.tarfield())  # 同案人输入框
        js = 'document.getElementById("jqDatedyjyksrq").removeAttribute("readonly")'
        self.driver.execute_script(js)  # 执行js脚本
        self.text_input('2019-09-20', ycjy.ksrq())  # 原羁押开始日期
        js = 'document.getElementById("jqDatedyjyjzrq").removeAttribute("readonly")'
        self.driver.execute_script(js)  # 执行js脚本
        self.text_input('2019-09-21', ycjy.jzrq())  # 原羁押截止日期




