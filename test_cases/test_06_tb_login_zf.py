import unittest
from base.browser_driver import BrowserDriver
from pages.ajxx_tb_page import AJXX_TB
from pages.home_page import HomePage
from pages.login_page import LoginPage
import logging
from common.logger import Logger
logger = Logger(logger='testcasezf').getlog()
logger.setLevel(level = logging.INFO)


class ResultTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'ga')  # 选择公安或者政法端进行登录,浏览器的选择在ini文件中进行配置

    def test_01_login_zfxt_zf(self):
        '''登陆政法端，查看页面展示和数据库中字段是否对应'''
        loginpage = LoginPage(self.driver)
        loginpage.login('wjjcyxun',123)#输入用户名和密码
        result=loginpage.is_login_sucess("苏州市吴江区人民检察院")
        self.assertTrue(result)
    def test_02_tb_enter_ajlist(self):
        '''进入提捕案件列表'''
        tb = HomePage(self.driver)
        tb.switch_iframe(0)
        logger.info("开始进入提捕流程")
        tb.clickTbBtn()#点击提捕标签
        try:
            assert "提捕" in self.get_page_title() # 获取页面标题
            logger.info("进入提捕业务成功")
        except Exception as e:
            logger.info("进入提捕业务失败，抛出异常:%s"%e)

    def test_03_ajmc_check(self):
        '''从页面获取案件状态和数据库进行对比'''
        tbajxx=AJXX_TB(self.driver)
        tbajxx.clickybajBtn()#点击已办案件列表
        tbajxx.clickfirstaj()#点击案件名称
        ajzt = self.driver.find_element_by_xpath(tbajxx.ajzt).text#获取页面元素内容
        logger.info("页面获取到的状态：%s" % ajzt)
        ajmc=self.driver.find_element_by_xpath(tbajxx.ajmc).get_attribute("value")
        logger.info("当前案件的案件名称为%s"%ajmc)
        assert "待审查" in ajzt


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)



