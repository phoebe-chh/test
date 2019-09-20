import logging
import os
import time

from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.ajxx_tb_page import TbAjxxPage
from pages.ajxx_ys_page import YsAjxxPage
from pages.jzxt_page import JzxtPage

logger = Logger(logger='jzxt').getlog()
logger.setLevel(level=logging.INFO)


class UploadFile(SeleniumDriver):
    """
    卷宗系统上传文书或卷宗操作
    """

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # 进入卷宗系统
    def enterjzxt_tb(self):
        wjgl=TbAjxxPage()  # 从案件信息页面点击文件管理按钮，进入卷宗系统页面
        self.click(wjgl.wjglbutton(),'xpath')
        time.sleep(3)

    def enterjzxt_ys(self):
        wjgl=YsAjxxPage()  # 从案件信息页面点击文件管理按钮，进入卷宗系统页面
        self.click(wjgl.wjglbutton(),'xpath')
        time.sleep(3)

    # 上传文书流程方法
    def uploadfile(self):
        logger.info("开始上传公安文书")
        jzxt = JzxtPage()  # 引入卷宗系统页面
        self.get_page_title()
        self.click(jzxt.gawsbutton(),'xpath')
        self.click(jzxt.uploadbutton(),'id')
        self.switch_iframe(1)
        self.double_click(jzxt.choosefileflashbutton(), 'xpath')
        os.popen(r'"F:\2019-06\autotest\upload.exe" "chrome" "F:\2019-06\autotest\起诉意见书.pdf"')
        time.sleep(5)
        all_input = self.driver.find_elements_by_tag_name("input")
        all_input[0].click()
        self.driver.switch_to.default_content()
        self.double_click(jzxt.firstfile(), 'xpath')
        self.switch_iframe(1)
        self.double_click(jzxt.confire_ws(),'xpath')
        time.sleep(10)

    # 上传卷宗等流程
    def uploadjz(self):
        logger.info("开始上传卷宗")
        jzxt=JzxtPage()  # 引入卷宗系统页面
        self.get_page_title() # 获取页面标题
        self.double_click(jzxt.jzroot(),'xpath')
        self.double_click(jzxt.jzadd(), 'xpath')
        self.double_click(jzxt.jzchild(), 'xpath')
        self.double_click(jzxt.uploadbutton(), 'id')
        self.switch_iframe(1)
        self.double_click(jzxt.choosefileflashbutton(), 'xpath')
        os.popen(r'"F:\2019-06\autotest\upload.exe" "chrome" "F:\2019-06\autotest\jz01.jpg"')
        time.sleep(5)
        self.double_click(jzxt.confire_jz(), 'xpath')
        time.sleep(5)

