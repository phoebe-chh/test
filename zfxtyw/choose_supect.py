import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from base.selenium_driver import SeleniumDriver
from common.logger import Logger
from pages.taq_tb_page import TbTaq
from pages.taq_ycjy_page import YcjyTaq

logger = Logger(logger='choosesupects').getlog()
logger.setLevel(level=logging.INFO)


class ChoosePeople(SeleniumDriver):
    """
    选择案件或者嫌疑人的类
    """

    # 在提案器中循环查找有嫌疑人的提捕案件
    def find_avaibale_tbaj(self):
        """
        提捕或者移诉提案器页面，在案件列表中选择有嫌疑人的案件，当页无可用案件则翻页查找
        最多翻页三次
        """
        taq = TbTaq()  # 实例化提捕提案器页面
        nextpagetime = 0  # 记录当前翻页的次数
        self.spsname = None
        flag = False  # 设置标签是否找到嫌疑人
        while nextpagetime <= 2 and flag == False:  # 最多翻页3次，如果翻页3次还找不到可以选择的案件，那么请排查数据
            ajtablelist = self.driver.find_element_by_id('caseGrid-table')
            table_aj_rows = ajtablelist.find_elements_by_tag_name('tr')
            ajnum = len(table_aj_rows) - 1  # 案件列表中案件的数量
            logger.info("当前页案件数量为%s" % ajnum)
            if ajnum >= 1 and ajnum <= 5:
                for cur_row in range(ajnum):
                    logger.info("正在查找第%s条案件" % (cur_row + 1))
                    spstablelist = self.driver.find_element_by_id('suspectGrid-table')
                    table_aj_rows = ajtablelist.find_elements_by_tag_name('tr')
                    logger.info("当前的案件列表数量为%s" % (len(table_aj_rows) - 1))
                    move = ajtablelist.find_elements_by_tag_name('tr')[cur_row + 1].find_elements_by_tag_name('td')[1]
                    logger.info("双击案件列表，寻找有嫌疑人的案件")
                    ActionChains(self.driver).double_click(move).perform()
                    time.sleep(2)
                    spec_rows = spstablelist.find_elements_by_tag_name('tr')
                    spec_now = spec_rows[1].find_elements_by_tag_name('td')
                    logger.info("正在查找的当前案件的嫌疑人数量为%s" % (len(spec_now) - 1))
                    # 判断是否有可选的嫌疑人
                    if len(spec_now) >= 2:  # 当前页能找到有嫌疑人的案件
                        logger.info("当前选择的这个案件有嫌疑人，结束寻找")
                        self.spsname = spec_rows[1].find_elements_by_tag_name('td')[1].text
                        logger.info('当前提捕流程选择的嫌疑人姓名： %s' % self.spsname)
                        self.click(taq.confirmbutton(), 'xpath')  # 勾选勾选框
                        logger.info("勾选成功")
                        self.click(taq.submitbutton(), 'xpath')  # 点击提交按钮
                        logger.info("提交成功")
                        flag = True  # 找到案件了，设置标签，结束循环
                        break
                    if cur_row == 4 and len(spec_now) < 2:  # 在当前页的最后一个案件都未发现嫌疑人则需要翻页
                        logger.info("当前页无可用案件，需要翻页查找")
                        self.click(taq.netpagebutton(), 'xpath')
                        nextpagetime = nextpagetime + 1
                        logger.info("开始翻页，当前为第%s次翻页，超过3次将不再继续翻页" % nextpagetime)
            else:
                logger.info("当前提案器中无案件，无法提案")

        return self.spsname  # 返回嫌疑人名称

    # 选择在押人员
    def find_zyry(self):
        taq = YcjyTaq()  # 实例化提案器页面
        ajtablelist = self.driver.find_element_by_id('jqGridBaseTable-table')
        table_aj_rows = ajtablelist.find_elements_by_tag_name('tr')
        ajnum = len(table_aj_rows) - 1  # 案件列表中案件的数量
        logger.info("当前页案件数量为%s" % ajnum)
        if ajnum >= 1:
            self.double_click(taq.checkradiobutton(), 'xpath')
            spsname = table_aj_rows[1].find_elements_by_tag_name('td')[3].text
            logger.info('当前提捕流程选择的嫌疑人姓名： %s' % spsname)
            self.click(taq.confirmbutton(), 'id')  # 点击确认添加按钮
            time.sleep(8)
        else:
            logger.info("当前提案器中无案件，无法提案")
