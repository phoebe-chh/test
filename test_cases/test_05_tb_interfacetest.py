import os
import unittest
import time
import logging

from datebase.database import DataBase
from datebase.getajid import GetAjid
from fileprocess.savedata import SaveResultToFile
from interface.post import ZfxtInterface
from logs.logger import Logger
logger = Logger(logger='callinterfacetest').getlog()
logger.setLevel(level = logging.INFO)


class InterfaceTest(unittest.TestCase):
    """
    调用接口，验证接口是否调用成功
    """
    def test_01_call_zf_interface(self):
        '''调用政法端的接口，验证接口是否调用成功'''
        # 验证返回结果是否是200,调用接口后停20s
        f = ZfxtInterface()
        result = f.post_main(104,'zf')
        # 判断接口返回的状态码是否是200
        self.assertEqual(200, result)
        time.sleep(20)

    def test_02_assert_interface_result(self):
        '''验证调用接口后，协同状态是否变成104'''
        # 连接数据库
        db=DataBase('ga')
        savedata = SaveResultToFile()
        ajid =savedata.readfile('ajid') # 从文件中读取ajid
        sql = "SELECT n_tbxtzt  FROM db_yw.t_tb_ajxx WHERE c_id LIKE '%s'"%(ajid)
        xtzt=db.getdata(sql,0)[1]
        logger.info("查询到的协同状态：%s"%xtzt)
        try:
            self.assertEqual(104,xtzt)
            logger.info('协同状态对比成功，当前协同状态%s' % xtzt)
        except Exception as e:
            logger.error('协同状态对比出错，错误信息：%s' % e)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    #运行单个用例
    # testunit=unittest.TestSuite()
    # testunit.addTest(InterfaceTest('test_02_assert_interface_result'))#添加测试用例方法名
    # runer=unittest.TextTestRunner(verbosity=2)
