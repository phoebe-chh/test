import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='wshy-ywlist').getlog()
logger.setLevel(level = logging.INFO)


class WshyYwListPage(ReadExcel):
    """
    说明：延长羁押业务列表页面
        通过pagename和elementname获取配置文件中的信息
    """

    # 网上换押列表添加在押人员按钮
    def addbutton(self):
        return self.get_element('ywlist_page_wshy','element1')

    # # 已办案件按钮
    # def ybajbutton(self):
    #     return self.get_element('ywlist_page_ycjy','element1')


