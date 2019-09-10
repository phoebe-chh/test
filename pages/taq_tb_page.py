import logging
from common.readexcel import ReadExcel
from logs.logger import Logger
logger = Logger(logger='taq_tb_page').getlog()
logger.setLevel(level = logging.INFO)


class TbTaq(ReadExcel):
    '''
    说明：
        提案器页面
    '''

    def confirmbutton(self):
        return self.get_element('taq_page','element1')

    def submitbutton(self):
        return self.get_element('taq_page','element2')

    def netpagebutton(self):
        return self.get_element('taq_page','element3')

    def ajtable(self):
        return self.get_element('taq_page', 'element4')

    def spstable(self):
        return self.get_element('taq_page', 'element5')
