import logging
import re
from base.selenium_driver import SeleniumDriver
from common.logger import Logger

logger = Logger(logger='get-ajid').getlog()
logger.setLevel(level=logging.INFO)


class GetAjidFromUrl(SeleniumDriver):
    """
    获取ajid的方法，在页面url中提取ajid
    参数：ajid坐在的坐标
    """

    def getajidfromurl(self, number):
        url = self.driver.current_url  # 获取当前页面的url，从url中提取ajid
        pattern = '\w{32}'  # 正则表达式，32位数字的单词，
        ajid = re.findall(pattern, url, flags=0)[number]  # 返回结果是个列表，ajid是列表中的第二个index
        if ajid is not None:
            logger.info("获取到的ajid为:{}".format(ajid))
            return ajid
        else:
            logger.info("ajid为空")
            return False

