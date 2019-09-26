import unittest
import logging
from datebase.database import DataBase
from fileprocess.savedata import SaveResultToFile
from common.logger import Logger

logger = Logger(logger='checkdatatest-202').getlog()
logger.setLevel(level=logging.INFO)


class CheckDataTest(unittest.TestCase):
    """
    检查案件状态是否正确，从数据库查询
    """

    def test_01_check_xtzt_ajid(self):
        """根据ajid查询当前案件状态是否正确(n_tbxtzt=202)"""
        db = DataBase('ga')
        savedata = SaveResultToFile()
        ajid = savedata.readfile('平台案件编号')
        sql = "SELECT n_ysxtzt  FROM db_yw.t_ys_ajxx WHERE c_id LIKE '%s'" % (ajid)
        xtzt = db.getdata(sql, 0)[1]
        logger.info("查询到的协同状态：%s" % xtzt)
        self.assertEqual(202, xtzt)  # 断言协同状态是否转换成功


if __name__ == '__main__':
    unittest.main(verbosity=2)
