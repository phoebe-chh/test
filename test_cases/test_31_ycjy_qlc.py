import time
import unittest
from zfxtyw.fill_ajxx import FillElementValue
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
from datebase.database import DataBase
from fileprocess.savedata import SaveResultToFile
from zfxtyw.addaj import AddAJ
from zfxtyw.choose_qzcs_type import ChooseQzcs
from zfxtyw.choose_supect import ChoosePeople
from pages.home_page import *
import logging
from common.logger import Logger
from zfxtyw.chooseywname import ChooseXtName
from zfxtyw.getajid import GetAjidFromUrl
from zfxtyw.jzxt_uploadfile import UploadFile
from zfxtyw.login import LoginPageTest
from zfxtyw.start_yw import StartYw
logger = Logger(logger='ys-qlc').getlog()
logger.setLevel(level=logging.INFO)


class YcjyTest(unittest.TestCase):
    """
    延长羁押完整流程测试
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'ga')  # 选择公安或者政法端进行登录,浏览器的选择在ini文件中进行配置

    def switch_window(self, number):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[number])

    def test_01_login(self):
        """登陆"""
        loginpage = LoginPageTest(self.driver)
        loginpage.login('241808', '123')  # 使用登陆方法
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        result = po.is_element_exist('//*[@id="identify"]', "xpath")  # 通过登陆后的单位判断是否登陆成功
        self.assertTrue(result)

    def test_02_enter_ycjy_ajlist(self):
        """进入延长羁押案件列表"""
        xtname = ChooseXtName(self.driver)
        xtname.switch_iframe(0)
        xtname.choose_ycjy()  # 选择进入延长羁押业务
        assert "延长羁押" in xtname.get_page_title()

    def test_03_ycjy_addaj(self):
        """点击选择案件，选择在押人员"""

        add = AddAJ(self.driver)
        add.add_ycjy_aj()  # 点击添加案件按钮
        iframe2 = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.switch_to.frame(iframe2)
        logger.info("开始选择案件和嫌疑人")
        cp = ChoosePeople(self.driver)  # 开始选择案件
        xyrxm = cp.find_zyry()  # 调用查找案件的方法
        self.assertIsNotNone(xyrxm)  # 断言嫌疑人是否找到
        savedata = SaveResultToFile()
        savedata.writefile('嫌疑人姓名', xyrxm)  # 写入文件

    def test_04_ycjy_fill_data(self):
        """进入延长羁押案件信息页面，填写必填项"""
        ycjy = FillElementValue(self.driver)
        ycjy.fill_ycjy_ajxx()  # 调用填写案件信息的方法
        start = StartYw(self.driver)
        start.save_ycjy()  # 点击送达按钮

    def test_05_jzxt_uploadfile(self):
        """进入卷宗系统，上传文书和卷宗"""
        zjxt = UploadFile(self.driver)
        zjxt.enterjzxt_ycjy()  # 进入文件管理页面
        self.switch_window(1)  # 需要切换窗口
        zjxt.uploadfile(r"F:\2019-06\autotest\延长羁押拘留期限通知书.pdf")
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        self.driver.switch_to.default_content()
        resultoffile = po.is_element_exist('jqTreeAreaFiles_ztree_4_span', "id")
        self.assertTrue(resultoffile)  # 断言文书上传结果
        self.switch_window(0)  # 切回延长羁押页面
        time.sleep(5)

    def test_06_get_ajid(self):
        """从页面url获取ajid，并保存到文件中"""
        ajid = GetAjidFromUrl(self.driver).getajidfromurl(1)
        sa = SaveResultToFile()
        sa.writefile('ajid', ajid)  # 获取页面ajid并写入文件
        result = sa.readfile('ajid')
        self.assertIsNotNone(result)  # 断言ajid是否存入成功

    def test_08_start_ycjy(self):
        """点击延长羁押按钮，发起延长羁押,至此公安端页面操作结束"""
        start = StartYw(self.driver)  # 点击送达按钮
        start.start_ycjy()
        logger.info(self.driver.title)
        assert "延长羁押" in self.driver.title  # 如果提起成功，页面跳转到延长羁押列表

    def test_09_tb_save_all_data(self):
        """保存所有数据到logs/record.txt中，至此公安端页面操作结束"""
        savedata = SaveResultToFile()
        ajid = savedata.readfile('ajid')
        xyrxm = savedata.readfile('嫌疑人姓名')
        self.assertIsNotNone(ajid)  # 断言是否读取到ajid
        savedata.clearfile()  # 清除之前的测试数据
        savedata.writefile('嫌疑人姓名', xyrxm)
        db = DataBase("ga")  # 链接数据库，选择ga端，数据库信息在ini文件中读取
        sql_ajcm = "SELECT  ajxx.c_ajmc  FROM db_yw.t_ycjy_ajxx  ajxx WHERE c_id='%s'" % (ajid)  # 通过sql查询ajmc
        ajmc = db.getdata(sql_ajcm, 0)[1]  # 执行sql
        savedata.writefile('案件名称', ajmc)
        savedata.writefile('平台案件编号', ajid)
        sql_jcajid = "SELECT  ajxx.c_jcajid  FROM db_yw.t_ycjy_ajxx  ajxx WHERE c_id='%s'" % (ajid)
        jcajid = db.getdata(sql_jcajid, 0)[1]  # 执行sql
        savedata.writefile('平台案件关联编号', jcajid)
        sql_jsdw = "SELECT corp.c_alias alise_js FROM db_yw.t_ycjy_ajxx ajxx JOIN db_uim.t_aty_corp corp " \
                   "ON ajxx.c_sskss = corp.c_id WHERE ajxx.c_id =  '%s' " % (ajid)
        jsdw = db.getdata(sql_jsdw, 0)[1]  # 执行sql
        savedata.writefile('接收单位编号', jsdw)
        sql_fsdw = "SELECT corp.c_alias alise_fs FROM db_yw.t_ycjy_ajxx ajxx JOIN " \
                   "db_uim.t_aty_corp corp ON ajxx.c_xtfqdw = corp.c_id WHERE ajxx.c_id = '%s'" % (ajid)
        fsdw = db.getdata(sql_fsdw, 0)[1]
        savedata.writefile('发送单位编号', fsdw)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # 运行所有
    # unittest.main(verbosity=2)
    # #运行单个用例
    testunit = unittest.TestSuite()
    testunit.addTest(YcjyTest('test_01_login'))  # 添加测试用例方法名
    testunit.addTest(YcjyTest('test_02_enter_ycjy_ajlist'))  # 添加测试用例方法名
    testunit.addTest(YcjyTest('test_03_ycjy_addaj'))  # 添加测试用例方法名
    testunit.addTest(YcjyTest('test_04_ycjy_fill_data'))
    testunit.addTest(YcjyTest('test_05_jzxt_uploadfile'))
    testunit.addTest(YcjyTest('test_06_get_ajid'))
    testunit.addTest(YcjyTest('test_08_start_ycjy'))
    testunit.addTest(YcjyTest('test_09_tb_save_all_data'))
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(testunit)
    # # #
