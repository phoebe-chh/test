import time
import unittest

import jpype

from datebase.database import DataBase

from fileprocess.savedata import SaveResultToFile

from fileprocess.encryption import Encryption
from fileprocess.putonserver import PutOnService
from fileprocess.replacefilecontent import ReplaceFileContent
from fileprocess.zipallfile import ZipAllFile
import logging
from common.logger import Logger
logger = Logger(logger='fileprocess-106').getlog()
logger.setLevel(level=logging.INFO)


class FileProcess(unittest.TestCase):
    """
    文件操作，包括替换xml文件内容，加密，并上传到服务器
    """
    def test_01_get_xyrxm(self):
        """获取嫌疑人姓名,并生成pdf文件名称"""
        savedata = SaveResultToFile()
        ajid = savedata.readfile('平台案件关联编号')
        sql_ajcm = "SELECT  xyr.c_xyrxm  FROM db_yw.t_jc_gaxyr  xyr WHERE c_id_ajxx='%s'" % (ajid)  # 通过sql查询ajmc
        db = DataBase("ga")
        xyrxm = db.getdata(sql_ajcm, 0)[1]  # 执行sql
        savedata.writefile('嫌疑人姓名', xyrxm)
        savedata.writefile('处理结果', 1)  # 添加106流程的处理结果,用来做替换
        savedata.writefile('文件显示名称', "\批准逮捕决定书"+'('+xyrxm+')'+'.pdf')  # 添加106流程的处理结果,用来做替换
        savedata.writefile('文件路径', "\ws"+"\批准逮捕决定书"+'('+xyrxm+')'+'.pdf')  # 添加106流程的处理结果,用来做替换

    def test_02_change_file_name(self):
        """修改pdf文件名称"""
        rn = ReplaceFileContent()
        savedata = SaveResultToFile()
        xyrxm = savedata.readfile('嫌疑人姓名')
        rn.rename_pdf(106,xyrxm)  # 修改pdf名称的方法，把嫌疑人姓名拼接到pdf文件名上

    def test_03_replace_xml(self):
        """替换xml文件内容并生成新xml"""
        f = ReplaceFileContent()
        f.getnodename()  # 从record.txt中获取替换节点名称
        f.getnodecontent()  # 从record.txt获取替换节点内容
        f.replace_content('106')  # 替换的xml文件，参数为流程编号

    def test_04_file_zip(self):
        """压缩某个文件夹下的文件，生成zip包"""
        z = ZipAllFile()
        z.zip_file(106)  # 压缩文件，参数为流程编号

    def test_05_encryption_zip(self):
        """加密压缩包"""
        f = Encryption()
        f.encryption_zip(106)  # 加密压缩包，参数为流程编号

    def test_06_put_on_server(self):
        """放在服务器路径上"""
        f = PutOnService('ga')
        f.putto_server('106')  # 推送压缩包，参数为流程编号
        time.sleep(5)  # 等待系统处理


if __name__ == '__main__':
    unittest.main(verbosity=2)
