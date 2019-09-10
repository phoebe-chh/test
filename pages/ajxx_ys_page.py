import logging
from common.readexcel import ReadExcel
from logs.logger import Logger
logger = Logger(logger='ajxx_ys_page').getlog()
logger.setLevel(level = logging.INFO)


class YsAjxxPage(ReadExcel):
    '''
    说明：
        通过ajxx_ys和elementname获取配置文件中的信息,返回元素路径
    '''

    def wjglbutton(self):
        return self.get_element('ajxx_ys','element1')

    def qzcscell(self):
        return self.get_element('ajxx_ys','element3')

    def qzscbutton(self):
        return self.get_element('ajxx_ys','element4')

    def qzsclist(self):
        return self.get_element('ajxx_ys','element5')

    def qzscfirst(self):
        return self.get_element('ajxx_ys','element6')

    def qzscconfirebutton(self):
        return self.get_element('ajxx_ys','element7')

    def savebutton(self):
        return self.get_element('ajxx_ys','element8')

    def subbitbutton(self):
        return self.get_element('ajxx_ys','element9')

    def ajmcfield(self):
        return self.get_element('ajxx_ys', 'element10')

    def xyrxmfield(self):
        return self.get_element('ajxx_ys', 'element11')

    def wpjsinputbox(self):
        return self.get_element('ajxx_ys', 'element12')

    def wswhinputbox(self):
        return self.get_element('ajxx_ys', 'element13')

    def ybajbutton(self):
        return self.get_element('ajxx_ys', 'element14')

    def ybajlist(self):
        return self.get_element('ajxx_ys', 'element15')

    # 点击提起移诉后，弹出页面的确认提起按钮
    def confirmbutton(self):
        return self.get_element('ajxx_ys', 'element16')














