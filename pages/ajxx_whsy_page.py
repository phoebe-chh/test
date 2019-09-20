import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='ajxx_wshy_page').getlog()
logger.setLevel(level=logging.INFO)


class WshyAjxxPage(ReadExcel):
    '''
    说明：
        通过ajxx_wshy和elementname获取配置文件中的信息,返回元素路径
    '''

    # 文件管理按钮
    def wjglbutton(self):
        return self.get_element('ajxx_wshy', 'element6')

    # 换押移送按钮
    def sendbutton(self):
        return self.get_element('ajxx_wshy', 'element5')

    # 保存按钮
    def savebutton(self):
        return self.get_element('ajxx_wshy', 'element7')

    # 同案人输入框
    def tarfield(self):
        return self.get_element('ajxx_wshy', 'element1')

    # 原羁押开始日期
    def ksrq(self):
        return self.get_element('ajxx_wshy', 'element2')

    # 原羁押截止日期
    def jzrq(self):
        return self.get_element('ajxx_wshy', 'element3')
