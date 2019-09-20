import logging
from common.readexcel import ReadExcel
from common.logger import Logger

logger = Logger(logger='taq_ycjy_page').getlog()
logger.setLevel(level=logging.INFO)


class YcjyTaq(ReadExcel):
    '''
    说明：
        延长羁押提案器页面
    '''

    # 单选按钮
    def checkradiobutton(self):
        return self.get_element('taq_ycjy_page', 'element2')

    # 确认添加按钮
    def confirmbutton(self):
        return self.get_element('taq_ycjy_page', 'element3')

    # def submitbutton(self):
    #     return self.get_element('taq_page', 'element2')
    #
    # def netpagebutton(self):
    #     return self.get_element('taq_page', 'element3')
    #
    # def ajtable(self):
    #     return self.get_element('taq_page', 'element4')
    #
    # def spstable(self):
    #     return self.get_element('taq_page', 'element5')
