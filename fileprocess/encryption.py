# coding:utf-8
import os
import jpype
import logging

from common.readconfig import ReadConfig
from common.logger import Logger

logger = Logger(logger='encryption').getlog()
logger.setLevel(level=logging.INFO)


class Encryption:
    """
    加密文件类
    参数：加密文件路径
    """

    def encryption_zip(self, xtbh):
        cg = ReadConfig()
        zippath = cg.getvalue('localPath', 'path') + '\\' + str(xtbh) + '.zip'
        logger.info(zippath)
        if os.path.exists(zippath):
            logger.info('压缩包存在，开始加密')
            jarpath1 = os.path.join(os.path.abspath('.'), '../tools//jar//ebcp-exchange-1.1.6-minio-SNAPSHOT.jar')
            jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath1))  # 启动jvm
            JClass = jpype.JClass('com.thunisoft.ebcp.exchange.support.utils.DESUtil')
            test = JClass()
            zipanme = os.path.split(zippath)[1]  # 获取压缩包名称
            logger.info("压缩包名称%s" % zipanme)
            zip_path = os.path.split(zippath)[0]  # 获取压缩包路径
            logger.info("压缩包路径%s" % zip_path)
            zip_path_after = os.path.join(zip_path, "./after_jiami")  # 默认在当前路径下创建一级目录，用来存放解密之后的压缩包
            test.encryptZip(zippath, zip_path_after, zipanme, "75AFFF024BDA72E9CAAB5E019BB94729")
            jpype.shutdownJVM()  # 最后关闭jvm
            logger.info("加密成功")
            logger.info("加密后文件存放路径：%s" % zip_path_after)
        else:
            logger.info('压缩包不存在，无法加密')

    # def closJvm(self):
    #     jpype.shutdownJVM()  # 最后关闭jvm


if __name__ == "__main__":
    f = Encryption()
    f.encryption_zip(104)
    # zippath = r"C:\Users\lenovo\Desktop\kkk\test\TB\104.zip"
    # f.encryption_zip(zippath)
