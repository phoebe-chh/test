import unittest
from base.browser_driver import BrowserDriver
from common.elementexist import ElemnetExist
from datebase.database import DataBase
from fileprocess.savedata import SaveResultToFile
from zfxtyw.addaj import AddTbAJ
from zfxtyw.choose_qzcs_type import ChooseQzcs
from zfxtyw.choose_supect import ChoosePeople
from pages.home_page import *
import logging
from common.logger import Logger
from zfxtyw.chooseywname import ChooseXtName
from zfxtyw.getajid import GetAjidFromUrl
from zfxtyw.jzxt_uploadfile import UploadFile
from zfxtyw.login import LoginPageTest
logger = Logger(logger='ys-qlc').getlog()
logger.setLevel(level=logging.INFO)


class YsTest(unittest.TestCase):
    """
    移诉完整流程测试
    """
    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.open_browser(browser, 'ga')  # 选择公安或者政法端进行登录,浏览器的选择在ini文件中进行配置

    def switch_window(self,number):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[number])

    def test_01_login(self):
        """登陆"""
        loginpage = LoginPageTest(self.driver)
        loginpage.login()  # 使用登陆方法
        po=ElemnetExist(self.driver)  # 实例化页面通用方法，判断登陆后的页面是否有某个元素
        result=po.is_element_exist('//*[@id="identify"]',"xpath")  # 通过登陆后的单位判断是否登陆成功
        self.assertTrue(result)

    def test_02_enter_tb_ajlist(self):

        """进入移诉案件列表"""
        tb = ChooseXtName(self.driver)
        tb.switch_iframe(0)
        tb.choose_ys()  # 选择进入移诉业务
        try:
            assert "移诉" in tb.get_page_title()  # 获取页面标题,判断是否登陆成功
            logger.info("进入移诉业务成功")
        except Exception as e:
            logger.info("进入移诉业务失败，抛出异常:%s"%e)

    def test_03_tb_addtbaj(self):

        """点击选择案件，进入提案器"""

        choosepeople = AddTbAJ(self.driver)
        choosepeople.addtbaj()  # 点击添加案件按钮
        iframe2 = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.switch_to.frame(iframe2)
        logger.info("开始选择案件和嫌疑人")
        cp=ChoosePeople(self.driver)  # 开始选择案件
        cp.find_avaibale_tbaj()  # 调用查找嫌疑人的方法

    # def test_04_fill_in_value(self):
    #
    #     """进入移诉页面，填写字段信息"""
    #
    #     tb = FillElementValue(self.driver)
    #     tb.fill_in_tb_ajxx()  # 填写页面字段内容
    #     logger.info('页面字段内容填写结束')

    def test_04_tb_chooseqzcs(self):

        """进入移诉页面，选择强制措施并保存"""
        tbaj = ChooseQzcs(self.driver)
        tbaj.chooseqzcs_ys() # 调用选择强制措施方法
        logger.info('强制措施选择结束')

    def test_05_jzxt_uploadfile(self):

        """进入卷宗系统，上传文书和卷宗"""
        zjxt = UploadFile(self.driver)
        zjxt.enterjzxt_ys()  # 进入文件管理页面
        self.switch_window(1)  # 需要切换窗口
        zjxt.uploadfile()  # 上传文书方法
        self.driver.switch_to.default_content()
        zjxt.uploadjz()  # 上传卷宗方法
        self.switch_window(0)  # 切回移诉页面

    def test_06_get_ajid(self):
        """从页面url获取ajid，并保存到文件中"""
        ajid = GetAjidFromUrl(self.driver).getajidfromurl(1)
        sa=SaveResultToFile()
        sa.writefile('ajid',ajid)  # 获取页面ajid并写入文件

    def test_07_set_qzzt(self):

        """设置签章状态为1，通过ajid查询数据库，设置n_yqz=1"""
        # 设置签章状态的sql
        ajid=SaveResultToFile().readfile('ajid')
        sql = "update db_jz.t_jzgl_wj set n_yqz =1 WHERE c_ywid='%s' and c_store_path is not null"%(ajid)
        # 链接数据库执行sql
        db = DataBase("ga")  # 链接数据库，选择ga端，数据库信息在ini文件中读取
        db.exe_update(sql)  # 执行sql

    def test_08_tb_goys(self):
        """点击移诉按钮，发起移诉,至此公安端页面操作结束"""

        ys = ChooseQzcs(self.driver)
        ys.start_ys()  # 发起移诉流程

    def test_09_tb_save_all_data(self):
        """保存所有数据到logs/record.txt中，至此公安端页面操作结束"""
        savedata = SaveResultToFile()
        ajid =savedata.readfile('ajid')
        db = DataBase("ga")  # 链接数据库，选择ga端，数据库信息在ini文件中读取
        sql_ajcm="SELECT  ajxx.c_ajmc  FROM db_yw.t_ys_ajxx  ajxx WHERE c_id='%s'"%(ajid) # 通过sql查询ajmc
        ajmc=db.getdata(sql_ajcm,0)[1]  # 执行sql
        savedata.writefile('案件名称',ajmc)
        savedata.writefile('平台案件编号',ajid)
        sql_jcajid = "SELECT  ajxx.c_jcajid  FROM db_yw.t_ys_ajxx  ajxx WHERE c_id='%s'" % (ajid)
        jcajid = db.getdata(sql_jcajid,0)[1]   # 执行sql
        savedata.writefile('平台案件关联编号',jcajid)
        sql_jsdw = "SELECT corp.c_alias alise_js FROM db_yw.t_ys_ajxx ajxx JOIN db_uim.t_aty_corp corp " \
                   "ON ajxx.c_jcyjsdw = corp.c_id WHERE ajxx.c_id =  '%s' " % (ajid)
        jsdw = db.getdata(sql_jsdw,0)[1]   # 执行sql
        savedata.writefile('接收单位编号', jsdw)
        sql_fsdw="SELECT corp.c_alias alise_fs FROM db_yw.t_ys_ajxx ajxx JOIN " \
                 "db_uim.t_aty_corp corp ON ajxx.c_gaysdw = corp.c_id WHERE ajxx.c_id = '%s'" % (ajid)
        fsdw=db.getdata(sql_fsdw,0)[1]
        savedata.writefile('发送单位编号',fsdw)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    #运行所有
    unittest.main(verbosity=2)
    # #运行单个用例
    # testunit=unittest.TestSuite()
    # testunit.addTest(YsTest('test_09_tb_save_all_data'))#添加测试用例方法名
    # runer=unittest.TextTestRunner(verbosity=2)
    # runer.run(testunit)
    # # #


