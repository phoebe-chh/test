import logging
import time

from base.selenium_driver import seleniumDriver
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='commenttest').getlog()
logger.setLevel(level=logging.INFO)


class AutoTest(seleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # 通过配置文件获取元素位置、定位方式、操作方式
    def autotest(self, testcasename):
        readconfig = ReadExcel()
        caseindex = readconfig.testcase_name(testcasename)
        lcoaltemodel = readconfig.lcoalte_model()
        testdata = readconfig.test_data()
        operatemethod = readconfig.operate_method()
        elepath = readconfig.element_path()
        pausetime =readconfig.pause_time()
        logger.info(caseindex)
        logger.info("当前测试用例所在的行数:" + ','.join([str(i)for i in caseindex]))
        for i in range(len(caseindex)):
            if operatemethod[i] == "sendkeys":
                self.text_input(testdata[i], elepath[i], lcoaltemodel[i])
                time.sleep(pausetime[i])
            elif operatemethod[i] == "click":
                self.click(elepath[i], lcoaltemodel[i])
                time.sleep(pausetime[i])
            elif operatemethod[i] == "doubleclick":
                self.double_click(elepath[i], lcoaltemodel[i])
                time.sleep(pausetime[i])
            else:
                logger.info("当前操作不支持")






