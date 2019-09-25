import time
import unittest

import jpype

from fileprocess.encryption import Encryption
from fileprocess.putonserver import PutOnService
from fileprocess.replacefilecontent import ReplaceFileContent
from fileprocess.zipallfile import ZipAllFile
import logging
from common.logger import Logger
logger = Logger(logger='fileprocess-104').getlog()
logger.setLevel(level=logging.INFO)


class FileProcess(unittest.TestCase):
    """
    文件操作，包括替换xml文件内容，加密，并上传到服务器
    """

    def test_01_replace_xml(self):
        """替换xml文件内容并生成新xml"""
        f = ReplaceFileContent()
        f.getnodename()  # 从record.txt中获取替换节点名称
        f.getnodecontent()  # 从record.txt获取替换节点内容
        f.replace_content('104')  # 替换的xml文件，参数为流程编号

    def test_02_file_zip(self):
        """压缩某个文件夹下的文件，生成zip包"""
        z = ZipAllFile()
        z.zip_file(104)  # 压缩文件，参数为流程编号

    def test_03_encryption_zip(self):
        """加密压缩包"""
        f = Encryption()
        f.encryption_zip(104)  # 加密压缩包，参数为流程编号

    def test_04_put_on_server(self):
        """放在服务器路径上"""
        f = PutOnService('ga')
        f.putto_server('104')  # 推送压缩包，参数为流程编号
        time.sleep(5)  # 等待系统处理


if __name__ == '__main__':
    unittest.main(verbosity=2)
