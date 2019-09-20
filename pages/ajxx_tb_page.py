import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='ajxx_tb_page').getlog()
logger.setLevel(level = logging.INFO)


class TbAjxxPage(ReadExcel):
    '''
    说明：
        通过ajxx_tb和elementname获取配置文件中的信息,返回元素路径
    '''

    def wjglbutton(self):
        return self.get_element('ajxx_tb','element1')

    # def xyrlist(self):
    #     return self.get_element('ajxx_tb','element2')

    def qzcscell(self):
        return self.get_element('ajxx_tb','element3')

    def qzscbutton(self):
        return self.get_element('ajxx_tb','element4')

    def qzsclist(self):
        return self.get_element('ajxx_tb','element5')

    def qzscfirst(self):
        return self.get_element('ajxx_tb','element6')

    def qzscconfirebutton(self):
        return self.get_element('ajxx_tb','element7')

    def savebutton(self):
        return self.get_element('ajxx_tb','element8')

    def subbitbutton(self):
        return self.get_element('ajxx_tb','element9')

    def ajmcfield(self):
        return self.get_element('ajxx_tb', 'element10')

    def xyrxmfield(self):
        return self.get_element('ajxx_tb', 'element11')

    def wpjsinputbox(self):
        return self.get_element('ajxx_tb', 'element12')

    def wswhinputbox(self):
        return self.get_element('ajxx_tb', 'element13')

    def ybajbutton(self):
        return self.get_element('ajxx_tb', 'element14')

    def ybajlist(self):
        return self.get_element('ajxx_tb', 'element15')











