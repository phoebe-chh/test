import time
import unittest
from fileprocess.savedata import SaveResultToFile
from zfxtyw.chooseywname import ChooseXtName
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
from zfxtyw.jzxt_uploadfile import UploadFile
from zfxtyw.login import LoginPageTest
from zfxtyw.search_aj import SearchAJ


class ResultCheck(unittest.TestCase):
    """
    登陆政法端检查接收方系统是否接收到数据
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'zf')  # 政法端进行登录

    def switch_window(self, number):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[number])

    def test_01_login_ga(self):
        """登陆政法端，查看页面展示和数据库中字段是否对应"""
        loginpage = LoginPageTest(self.driver)
        loginpage.login('wjjcyzj1', '123')  # 使用登陆方法
        po = ElemnetExist(self.driver)
        result = po.is_element_exist('//*[@id="identify"]', "xpath")  # 通过登陆后的单位判断是否登陆成功
        self.assertTrue(result)

    def test_02_enter_tb_ajlist(self):
        """进入提捕案件列表"""
        tb = ChooseXtName(self.driver)
        tb.switch_iframe(0)
        tb.choose_tb()  # 选择进入提捕业务
        assert "提捕案件列表" in tb.get_page_title()  # 断言是否进入提捕页面

    def test_03_find_tb_ajmc(self):
        """查看当前嫌疑人是否能查到"""
        aj = SearchAJ(self.driver)
        savedata = SaveResultToFile()
        xyrxm = savedata.readfile('嫌疑人姓名')  # 读取之前提捕的嫌疑人姓名
        self.assertIsNotNone(xyrxm)  # 断言嫌疑人姓名是否为空
        aj.search_tbxyrxm(xyrxm)  # 用该嫌疑人姓名查询
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        xyrxminlist = po.is_table_data_exist('caseGrid-table', 4)  # 获取当前列表中该列的值
        self.assertEqual(xyrxminlist, xyrxm)  # 断言强制措施中的内容是否有值
        ajzt = po.is_table_data_exist('caseGrid-table', 15)
        self.assertEqual(ajzt, '待受理')

    def test_04_check_file(self):
        """进入卷宗系统，检查文书和卷宗是否存在"""
        sj = SearchAJ(self.driver)
        sj.enter_tbajxx()  # 进入案件信息页面
        zjxt = UploadFile(self.driver)
        zjxt.enterjzxt_tb()
        self.switch_window(1)  # 需要切换窗口
        time.sleep(3)
        filename = self.driver.find_element_by_xpath('//*[@id="jqTreeAreaFiles_ztree_3_span"]').text
        self.assertEqual(filename, '公安文书(1)')
        jzname = self.driver.find_element_by_xpath('//*[@id="jqTreeAreaFiles_ztree_7_span"]').text
        self.assertEqual(jzname, '批捕卷宗(1)')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # 运行所有
    unittest.main(verbosity=2)
