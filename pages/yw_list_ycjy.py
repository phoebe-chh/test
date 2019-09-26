import logging
from common.readexcel import ReadExcel
from common.logger import Logger

logger = Logger(logger='ycjy-ywlist').getlog()
logger.setLevel(level=logging.INFO)


class YcjyYwListPage(ReadExcel):
    """
    说明：延长羁押业务列表页面
        通过pagename和elementname获取配置文件中的信息
    """

    # 延长羁押列表
    def tblist(self):
        return self.get_element('ywlist_page_ycjy', 'element2')

    # 延长羁押列表添加在押人员按钮
    def addbutton(self):
        return self.get_element('ywlist_page_ycjy', 'element1')

    # 嫌疑人查询框
    def xyrtext(self):
        return self.get_element('ywlist_page_ycjy','element3')

    # 查询按钮
    def searchbutton(self):
        return self.get_element('ywlist_page_ycjy','element4')
