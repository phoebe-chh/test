import logging

from common.readexcel import ReadExcel
from logs.logger import Logger
logger = Logger(logger='jzxtpage').getlog()
logger.setLevel(level = logging.INFO)

class JzxtPage(ReadExcel):

    """
    说明：
        卷宗系统按钮,包括各种上传按钮和插件
    """
    def wjglbutton(self):
        return self.get_element('jzxt_page','element1')

    def gawsbutton(self):
        return self.get_element('jzxt_page','element2')

    def uploadbutton(self):
        return self.get_element('jzxt_page','element3')

    def choosefileflashbutton(self):
        return self.get_element('jzxt_page','element4')

    def filetypebutton(self):
        return self.get_element('jzxt_page','element5')

    def firstfile(self):
        return self.get_element('jzxt_page','element6')

    def confire_ws(self):
        return self.get_element('jzxt_page','element7')

    def jzroot(self):
        return self.get_element('jzxt_page','element8')

    def jzadd(self):
        return self.get_element('jzxt_page','element9')

    def jzchild(self):
        return self.get_element('jzxt_page', 'element10')

    def confire_jz(self):
        return self.get_element('jzxt_page', 'element11')

    def savebutton(self):
        return self.get_element('jzxt_page', 'element2')


