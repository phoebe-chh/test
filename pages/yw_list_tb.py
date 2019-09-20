import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='tbywlist').getlog()
logger.setLevel(level = logging.INFO)


class TbYwListPage(ReadExcel):
    """
    说明：提捕业务页面
        通过pagename和elementname获取配置文件中的信息
    """

    # 提捕列表
    def tblist(self):
        return self.get_element('ywlist_page_tb','element2')

    # 添加案件按钮
    def addbutton(self):
        return self.get_element('ywlist_page_tb','element3')

    # 已办案件按钮
    def ybajbutton(self):
        return self.get_element('ywlist_page_tb','element1')


