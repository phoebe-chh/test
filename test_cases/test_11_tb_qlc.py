import time
import unittest
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
from datebase.database import DataBase
from datebase.updateqzzt import UpdateQzzt
from fileprocess.savedata import SaveResultToFile
from zfxtyw.addaj import AddAJ
from zfxtyw.choose_qzcs_type import ChooseQzcs
from zfxtyw.choose_supect import ChoosePeople
from pages.home_page import *
import logging
from common.logger import Logger
from zfxtyw.chooseywname import ChooseXtName
from zfxtyw.fill_ajxx import FillElementValue
from zfxtyw.getajid import GetAjidFromUrl
from zfxtyw.jzxt_uploadfile import UploadFile
from zfxtyw.login import LoginPageTest
from zfxtyw.start_yw import StartYw

logger = Logger(logger='tb-qlc').getlog()
logger.setLevel(level=logging.INFO)


class TbTest(unittest.TestCase):
    """
    提捕完整流程测试
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
        loginpage.login()  # 使用登陆方法
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        result = po.is_element_exist('//*[@id="identify"]', "xpath")  # 通过登陆后的单位判断是否登陆成功
        self.assertTrue(result)  # 断言登陆结果

    def test_02_enter_tb_ajlist(self):
        """进入提捕案件列表"""
        tb = ChooseXtName(self.driver)
        tb.switch_iframe(0)
        tb.choose_tb()  # 选择进入提捕业务
        assert "提捕" in tb.get_page_title()  # 断言是否进入提捕页面

    def test_03_tb_addtbaj(self):
        """点击选择案件,进入提案器"""

        choosepeople = AddAJ(self.driver)
        choosepeople.add_tb_aj()  # 点击添加案件按钮
        iframe2 = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.switch_to.frame(iframe2)
        logger.info("开始选择案件和嫌疑人")
        cp = ChoosePeople(self.driver)  # 开始选择案件
        result = cp.find_avaibale_tbaj()  # 调用查找嫌疑人的方法
        self.assertTrue(result)  # 断言是否找到嫌疑人方法的返回结果

    def test_04_fill_in_value(self):
        """进入提捕页面，填写字段信息"""

        tb = FillElementValue(self.driver)
        tb.fill_in_tb_ajxx()  # 填写页面字段内容
        logger.info('页面字段内容填写结束')

    def test_05_tb_chooseqzcs(self):
        """进入提捕页面，选择强制措施并保存"""
        tbaj = ChooseQzcs(self.driver)
        tbaj.chooseqzcs_tb()  # 调用选择强制措施方法
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        result = po.is_table_data_exist('suspectGrid-table', 4)  # 获取当前列表中该列的值
        self.assertTrue(result)  # 断言强制措施中的内容是否有值

    def test_05_jzxt_uploadfile(self):
        """进入卷宗系统，上传文书和卷宗"""
        zjxt = UploadFile(self.driver)
        zjxt.enterjzxt_tb()  # 进入文件管理页面
        self.switch_window(1)  # 需要切换窗口
        zjxt.uploadfile(r"F:\2019-06\autotest\起诉意见书.pdf")  # 上传文书，传入文书路径
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        # 断言卷宗是否上传成功
        self.driver.switch_to.default_content()
        resultoffile = po.is_element_exist('jqTreeAreaFiles_ztree_4_span', "id")
        self.assertTrue(resultoffile)  # 断言上传结果
        zjxt.uploadjz(r"F:\2019-06\autotest\jz01.jpg")  # 上传卷宗方法
        resultojz = po.is_element_exist('jqTreeAreaFiles_ztree_8_span', "id")
        self.assertTrue(resultojz)
        self.switch_window(0)  # 切回提捕页面
        # 断言是否上传卷宗成功

    def test_06_get_ajid(self):
        """从页面url获取ajid，并保存到文件中"""
        ajid = GetAjidFromUrl(self.driver).getajidfromurl(1)
        self.assertIsNotNone(ajid)  # 断言是否获取到ajid
        sa = SaveResultToFile()
        sa.writefile('ajid', ajid)  # 获取页面ajid并写入文件

    def test_07_set_qzzt(self):
        """设置签章状态为1，通过ajid查询数据库，设置n_yqz=1"""
        # 设置签章状态的sql
        ajid = SaveResultToFile().readfile('ajid')
        sql = "update db_jz.t_jzgl_wj set n_yqz =1 WHERE c_ywid='%s' and c_store_path is not null" % (ajid)
        # 链接数据库执行sql
        db = DataBase("ga")  # 链接数据库，选择ga端，数据库信息在ini文件中读取
        db.exe_update(sql)  # 执行sql

    def test_08_tb_gotibu(self):
        """点击提捕按钮，发起提捕,至此公安端页面操作结束"""

        tb = StartYw(self.driver)
        tb.start_tb()  # 发起提捕流程
        po = ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        result = po.is_alert_present()  # 判断是否有弹框，如果没有则认为提捕成功
        self.assertFalse(result)

    # 页面操作结束之后，保存数据库中字段内容到文件中，提供后续文件操作使用
    def test_09_tb_save_all_data(self):
        """保存所有数据到logs/record.txt中，至此公安端页面操作结束"""
        savedata = SaveResultToFile()
        ajid = savedata.readfile('ajid')
        savedata.clearfile()  # 清除之前的测试数据
        db = DataBase("ga")  # 链接数据库，选择ga端，数据库信息在ini文件中读取
        sql_ajcm = "SELECT  ajxx.c_ajmc  FROM db_yw.t_tb_ajxx  ajxx WHERE c_id='%s'" % (ajid)  # 通过sql查询ajmc
        ajmc = db.getdata(sql_ajcm, 0)[1]  # 执行sql
        savedata.writefile('案件名称', ajmc)
        savedata.writefile('平台案件编号', ajid)
        sql_jcajid = "SELECT  ajxx.c_jcajid  FROM db_yw.t_tb_ajxx  ajxx WHERE c_id='%s'" % (ajid)
        jcajid = db.getdata(sql_jcajid, 0)[1]  # 执行sql
        savedata.writefile('平台案件关联编号', jcajid)
        sql_jsdw = "SELECT corp.c_alias alise_js FROM db_yw.t_tb_ajxx ajxx JOIN db_uim.t_aty_corp corp " \
                   "ON ajxx.c_jcyjsdw = corp.c_id WHERE ajxx.c_id = '%s'" % (ajid)
        jsdw = db.getdata(sql_jsdw, 0)[1]  # 执行sql
        savedata.writefile('接收单位编号', jsdw)
        sql_fsdw = "SELECT corp.c_alias alise_fs FROM db_yw.t_tb_ajxx ajxx JOIN " \
                   "db_uim.t_aty_corp corp ON ajxx.c_gajysdw = corp.c_id WHERE ajxx.c_id = '%s'" % (ajid)
        fsdw = db.getdata(sql_fsdw, 0)[1]
        savedata.writefile('发送单位编号', fsdw)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # 运行所有
    # unittest.main(verbosity=2)
    # 运行单个用例
    testunit = unittest.TestSuite()
    testunit.addTest(TbTest('test_01_login'))  # 添加测试用例方法名
    testunit.addTest(TbTest('test_02_enter_tb_ajlist'))
    testunit.addTest(TbTest('test_03_tb_addtbaj'))
    testunit.addTest(TbTest('test_04_fill_in_value'))
    testunit.addTest(TbTest('test_05_tb_chooseqzcs'))
    # testunit.addTest(TbTest('test_05_jzxt_uploadfile'))
    # # # testunit.addTest(TbTest('test_07_set_qzzt'))
    # # # testunit.addTest(TbTest('test_09_tb_save_all_data'))
    testunit.addTest(TbTest('test_08_tb_gotibu'))
    # # # # test_09_tb_save_all_data
    # # # # testunit.addTest(TbTest('test_07_set_qzzt'))
    # # # # # # test_05_jzxt_uploadfile
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(testunit)
    # # #
