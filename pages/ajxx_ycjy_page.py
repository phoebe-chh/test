import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='ajxx_ycjy_page').getlog()
logger.setLevel(level = logging.INFO)


class YcjyAjxxPage(ReadExcel):
    '''
    说明：
        通过ajxx_ycjy和elementname获取配置文件中的信息,返回元素路径
    '''

    # 文件管理按钮
    def wjglbutton(self):
        return self.get_element('ajxx_ycjy','element6')

    # 送达看守所按钮
    def sendbutton(self):
        return self.get_element('ajxx_ycjy','element5')

    # 保存按钮
    def savebutton(self):
        return self.get_element('ajxx_ycjy','element7')

    # 同案人输入框
    def tarfield(self):
        return self.get_element('ajxx_ycjy', 'element1')

    # 原羁押开始日期
    def ksrq(self):
        return self.get_element('ajxx_ycjy', 'element2')

    # 原羁押截止日期
    def jzrq(self):
        return self.get_element('ajxx_ycjy', 'element3')














