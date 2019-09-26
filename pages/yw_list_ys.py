import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='ys-ywlist').getlog()
logger.setLevel(level = logging.INFO)


class YsYwListPage(ReadExcel):
    """
    说明：移诉业务页面
        通过pagename和elementname获取配置文件中的信息
    """

    # 移诉列表
    def yslist(self):
        return self.get_element('ywlist_page_ys','element2')

    # 添加案件按钮
    def addbutton(self):
        return self.get_element('ywlist_page_ys','element3')

    # 已办案件按钮
    def ybajbutton(self):
        return self.get_element('ywlist_page_ys','element1')

    # 查询嫌疑人姓名输入框
    def xyrxminputtext(self):
        return self.get_element('ywlist_page_ys','element4')

    # 查询按钮
    def searchbutton(self):
        return self.get_element('ywlist_page_ys','element5')


