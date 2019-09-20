import logging
from common.readexcel import ReadExcel
from common.logger import Logger
logger = Logger(logger='homepage').getlog()
logger.setLevel(level = logging.INFO)


class HomePage(ReadExcel):

    '''
    说明：
        通过pagename和elementname获取配置文件中的信息
    '''

    def tbyw(self):
        return self.get_element('homepage_ywlx','element1')  # 获取页面元素路径

    def ysyw(self):
        return self.get_element('homepage_ywlx','element2')  # 获取页面元素路径


