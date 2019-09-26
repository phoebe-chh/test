import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait

from base.selenium_driver import SeleniumDriver
from common.logger import Logger

logger = Logger(logger='element-exist').getlog()
logger.setLevel(level=logging.INFO)


class ElemnetExist(SeleniumDriver):
    """
    说明：
        页面通用方法，判断页面元素是否存在,如果不存在，截图保存
        参数：定位方式和元素位置

    """

    # 判断元素是否存在
    def is_element_exist(self, locator, locatorType='id'):
        flag = False
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((locatorType, locator)))
            logger.info("找到该元素")
            flag = True
        except TimeoutException:
            logger.info("在10s内无法定位到该元素，该元素不存在")
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('../errormg/%s.png' % nowtime)
        return flag

    # 判断元素是否可点击
    def is_element_locate(self, locator, locatorType='id'):
        pass

    # 判断某个列表中的数据是否为空,参数为当前表格的table标签id和当前需要定位的元素的序列号
    def is_table_data_exist(self, tablid, lownumber):
        tablelist = self.driver.find_element_by_id(tablid)
        rows = tablelist.find_elements_by_tag_name('tr')
        cell = rows[1].find_elements_by_tag_name('td')
        data = cell[lownumber].text
        logger.info("当前列表中的数据内容为{}".format(data))
        return data

    # 判断卷宗页面的文件是否存在,参数为当前父节点的id和当前定位的元素位置
    def is_file_exist(self, ulid, number):
        li_list = self.driver.find_element_by_id(ulid)  # jqTreeAreaFiles_ztree_3
        # rows = li_list.find_elements_by_tag_name('ul')  # 定位元素中的ul标签
        fileindex = li_list.find_elements_by_tag_name('li')  # 总共几个文件
        logger.info("当前上传的文书个数为：{}".format(len(fileindex)))
        aindex = fileindex[number].find_elements_by_tag_name('a')
        filename = aindex[1].find_elements_by_tag_name('span').text
        # filename = spanindex[number].text
        logger.info("当前上传的文书名称为：{}".format(filename))
        if filename is not None:
            return True
        else:
            return False

    # 判断某个操作是否有弹框
    def is_alert_present(self):
        result = EC.alert_is_present()
        if result:
            logger.info("有弹框")
            return True
        else:
            logger.info("正常")
            return False

    # # 判断页面元素是否加载
    # def is_element_locate(self):
    #     presence_of_all_elements_located
